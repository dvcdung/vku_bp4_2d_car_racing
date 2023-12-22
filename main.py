import pygame
from config.game_config import *
from src.game_manager import GameManager
from src.utils.app_network import Net

# Create a window
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("2D CAR RACING")

# setup game
game_manager = GameManager(screen)
game_manager.mode = 0
game_manager.map_id = "01"
game_manager.level = 0
game_manager.is_trainning = False

# net = Net()
# net.connect_to_server()

# net.send_to_server("0010", "dvc")
# while(True):
#     amount = net.receive_from_server
# net.send_to_server("0011", "dvc|hello")

# Run the game
game_manager.start_game()
# while(True):
#     pass