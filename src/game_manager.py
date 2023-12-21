import pygame
import sys
from src.game_objects.map import Map
from src.game_objects.car import Car
from config.game_config import *
import neat
import pickle

class GameManager:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.screen_size = screen.get_size()

        # Setup the game
        self.start_pos_dict = {"01": (-3900, -1200),}

        self.mod = 0        # 0: practice with AI, 1: multiplayer
        self.map_id = "01"
        self.level = 0      # 0: easy, 1: hard

        self.is_trainning = False

        # Create game objects for player
        self.map = Map(self.screen) # Using map.loadImage(map_id) to load map, default map01
        self.car = Car(self.screen) # Using car.loadImage(car_id) to load car, default car001
        self.car.velocity = GAME_SPEED

        # Data for game handling

    def start_game(self):
        # init objects
        clock = pygame.time.Clock()
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
        if self.mod == 0:
            # use neural network to control the car
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            output = net.activate(self.car.get_data())
            choice = output.index(max(output))
            if choice == 0:
                self.car.angle += ANGLE_UNIT
            elif choice == 1:
                self.car.angle -= ANGLE_UNIT

        # Update map object
        self.map.update(self.car)

        # Update car object
        self.car.update(self.map)
        genome.fitness = self.car.distance
        if not self.car.is_alive:
            if self.car.is_finished:
                # this line give priority to shorter distances 
                # by increasing fitness of genome
                genome.fitness = (100000 - genome.fitness)
            del self.car
            del self.map
            return False
        return True