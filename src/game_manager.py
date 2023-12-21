import pygame
import sys
from src.game_objects.map import Map
from src.game_objects.car import Car
from config.game_config import *
from src.utils.hand_controller import ThreadVideo
import neat
import pickle

class GameManager:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.screen_size = screen.get_size()

        # Setup the game
        self.start_pos_dict = {"01": (-3900, -1200),}
        self.mode = 0        # 0: practice with AI, 1: multiplayer
        self.map_id = "01"
        self.level = 0      # 0: easy, 1: hard
        self.is_trainning = False
        self.opponents = []
        self.num_alive = 0

    def init_game(self):
        # Create game objects for player
        self.map = Map(self.screen) # Using map.loadImage(map_id) to load map, default map01
        self.car = Car(self.screen) # Using car.loadImage(car_id) to load car, default car001
        self.car.loadImage("102")
        self.driver_frame = ThreadVideo()
        self.driver_frame.start()
        # self.car.velocity = GAME_SPEED
        # create game objects for other players
        map = Map(self.screen)
        car = Car(self.screen)
        car.velocity = GAME_SPEED
        self.opponents.append({"name": "bot_ai", "map": map, "car": car})

        # number of car still alive
        self.num_alive = len(self.opponents) + 1

    def start_game(self):
        clock = pygame.time.Clock()
        # init game
        self.init_game()

        # load Neat Config
        config_path =r"config/neat_config.txt"
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
        # get genome trained from file
        with open("config/best_genome_50.pkl", "rb") as file:
            loaded_genome = pickle.load(file)

        # run the game
        while (True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                    
            if not self.update(loaded_genome, config): break

            pygame.display.flip()
            clock.tick(50)

    # game with AI
    def update(self, genome, config):
        # handle event
        self.car.handle_events()
        # Update map object
        self.map.update(self.car)
        self.map.draw()

        for opponent in self.opponents:
            # use neural network to control the car
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            output = net.activate(opponent["car"].get_data())
            choice = output.index(max(output))
            if choice == 0:
                opponent["car"].angle += ANGLE_UNIT
            elif choice == 1:
                opponent["car"].angle -= ANGLE_UNIT
            opponent["map"].update(opponent["car"])
            opponent["car"].update(opponent["map"])
            opponent["car"].draw((
                opponent["car"].rect.topleft[0] - opponent["map"].start_pos[0] + self.map.start_pos[0],
                opponent["car"].rect.topleft[1] - opponent["map"].start_pos[1] + self.map.start_pos[1]
            ))
            genome.fitness = opponent["car"].distance

        # Update car object
        if self.car.is_alive:
            if self.driver_frame.dist == 2:
                self.car.angle -= ANGLE_UNIT
            elif self.driver_frame.dist == 1:
                self.car.angle += ANGLE_UNIT
            elif self.driver_frame.dist == 0:
                self.car.velocity = GAME_SPEED
            self.car.update(self.map)
            self.car.draw()

        # check the existence of car
        for opponent in self.opponents:
            if not opponent["car"].is_alive:
                del opponent["car"]
                del opponent["map"]
                self.num_alive -= 1
            if self.car.is_finished:
                # this line give priority to shorter distances 
                # by increasing fitness of genome
                genome.fitness = (100000 - genome.fitness)
        if not self.car.is_alive:
            self.num_alive -= 1
            if self.car.is_finished:
                pass
            # del self.car
            # del self.map
            # return False
        
        return True