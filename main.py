import pygame
import sys
from src.game_manager import GameManager

SCREEN_SIZE = (1200, 700)

# Create a window
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("2D CAR RACING")

# Create init objects
clock = pygame.time.Clock()
game_manager = GameManager(screen)

# Run the game
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    game_manager.update()

    pygame.display.flip()
    clock.tick(50)