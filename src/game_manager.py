import pygame
import sys
from src.game_objects.map import Map
from src.game_objects.car import Car
from config.game_config import *
from src.utils.hand_controller import ThreadVideo
from src.utils.app_network import Net
import neat
import pickle

class GameManager:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.screen_size = screen.get_size()

        # Setup the game
        self.current_player = {"user_id": 0, "username": "player"} # test
        self.start_pos_dict = {"01": (-3900, -1200),}
        self.mode = 0        # 0: practice with AI, 1: multiplayer
        self.map_id = "01"
        self.car_id = "001"
        self.level = 0      # 0: easy, 1: hard
        self.is_trainning = False
        self.is_playing = False
        self.num_alive = 0
        self.socket = None

    def start_game(self):
        self.is_playing = True
        clock = pygame.time.Clock()
        # init game
        self.winner = None
        if self.mode == 0:
            if self.level == 0:
                self.genome_path = "config/best_genome_10.pkl"  
            else: 
                self.genome_path = "config/best_genome_50.pkl"
            self.init_bot()
            self.num_alive = 2

        # Create game objects for player
        self.map = Map(self.screen) # Using map.loadImage(map_id) to load map, default map01
        self.car = Car(self.screen) # Using car.loadImage(car_id) to load car, default car001
        self.car.loadImage(self.car_id)

        # # display driver frame
        self.driver_frame = ThreadVideo()
        self.driver_frame.start()

        # load Neat Config
        config_path =r"config/neat_config.txt"
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
        # get genome trained from file
        with open(self.genome_path, "rb") as file:
            loaded_genome = pickle.load(file)

        # run the game
        while (self.num_alive > 0):
            self.num_alive = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.driver_frame.video_shower.stop()
                    self.driver_frame.video_getter.stop()
                    break
                        
            # handle event
            self.car.handle_events()
            # Update map object
            self.map.update(self.car)
            self.map.draw()

            if not self.mode == 1:
                self.update_bot(loaded_genome, config)
                    
            # Update car object
            if self.driver_frame.dist == 2:
                self.car.angle -= ANGLE_UNIT
            elif self.driver_frame.dist == 1:
                self.car.angle += ANGLE_UNIT
            elif self.driver_frame.dist == 0:
                self.car.velocity = GAME_SPEED
            self.car.update(self.map)
            self.car.draw()

            if self.car.is_alive:
                self.num_alive += 1
            elif self.car.is_finished:
                if not self.winner: self.winner = self.current_player["username"]
            
            pygame.display.flip()
            clock.tick(50)

        if not self.is_trainning:
            print(f"The winner is: {self.winner}")
            self.driver_frame.video_shower.stop()
            self.is_playing = False
            pygame.time.delay(2000)
            pygame.quit()
        

    def init_bot(self):
        # create game objects for other players
        map = Map(self.screen)
        car = Car(self.screen)
        car.velocity = GAME_SPEED
        self.bot = {"name": "Bot AI", "map": map, "car": car}

    # game with AI
    def update_bot(self, genome, config):
        # use neural network to control the car
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        output = net.activate(self.bot["car"].get_data())
        choice = output.index(max(output))
        
        if choice == 0:
            self.bot["car"].angle += ANGLE_UNIT
        elif choice == 1:
            self.bot["car"].angle -= ANGLE_UNIT
        self.bot["map"].update(self.bot["car"])
        self.bot["car"].update(self.bot["map"])
        if self.is_trainning:
            self.bot["map"].draw()
            self.bot["car"].draw_radars()
            self.bot["car"].draw((
                self.bot["car"].rect.topleft[0] - self.bot["map"].start_pos[0] + self.bot["map"].start_pos[0],
                self.bot["car"].rect.topleft[1] - self.bot["map"].start_pos[1] + self.bot["map"].start_pos[1]
            ))
        else:
            self.bot["car"].draw((
                self.bot["car"].rect.topleft[0] - self.bot["map"].start_pos[0] + self.map.start_pos[0],
                self.bot["car"].rect.topleft[1] - self.bot["map"].start_pos[1] + self.map.start_pos[1]
            ))
        genome.fitness = self.bot["car"].distance
        # check the existence of car
        if self.bot["car"].is_alive:
            self.num_alive += 1
        elif self.bot["car"].is_finished:
            if not self.is_trainning:
                if not self.winner: self.winner = self.bot["name"]
            # # for hard mode
            # # this line give priority to shorter distances
            # # by increasing fitness of genome
            # genome.fitness = (100000 - genome.fitness)
            # for easy mode
            pass