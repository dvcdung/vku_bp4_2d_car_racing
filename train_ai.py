import pygame
import sys
from config.game_config import *
from src.game_manager import GameManager
import neat
import pickle

# load config
config_path = r"config/neat_config.txt"
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
# create population and add reporters
population = neat.Population(config)
population.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
population.add_reporter(stats)

# Run the game
def run_simulation(genomes, config):
    pygame.init()
    # Create a window
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("2D CAR RACING")
    # Create init objects
    clock = pygame.time.Clock()

    for index, genome in genomes:
        genome.fitness = 0

        game_manager = GameManager(screen)
        game_manager.is_trainning = True
        game_manager.init_bot()
        game_manager.num_alive = 20

        while (game_manager.num_alive > 0):
            game_manager.num_alive = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            
            game_manager.update_bot(genome, config)

            pygame.display.flip()
            clock.tick(50)

best_genome = population.run(run_simulation, 10)
# Save best genome to file
with open("config/best_genome_10.pkl", "wb") as file:
    pickle.dump(best_genome, file)
