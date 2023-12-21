import pygame
import numpy as np
from config.game_config import *
from src.utils.image_handler import ImageHandler as imgHander

class Map:
    def __init__(self, screen: pygame.Surface):
        self.folder_path = "assets/maps/"
        self.screen = screen
        # map properties
        self.id = None
        self.image = None
        # location properties
        self.start_pos = (0, 0)
        # physical properties

        # initialization
        self.loadImage()
        
    def update(self, car):
        # update the map
        self.move(car)

    def draw(self):
        self.screen.blit(self.image, self.start_pos)

    def pos_in_image(self, pos):
        return (int(pos[0] - self.start_pos[0]), int(pos[1] - self.start_pos[1]))

    def loadImage(self, map_id="01", start_pos=(-3900, -1200)):
        self.start_pos = start_pos
        self.id = map_id
        self.image = imgHander.load(f"{self.folder_path}map{self.id}.png")

    def move(self, car):
        del_x = - car.velocity * np.cos(car.angle*np.pi/180)
        del_y = car.velocity * np.sin(car.angle*np.pi/180)
        self.start_pos = (self.start_pos[0] + del_x, self.start_pos[1] + del_y)

    def isInTrack(self, pos):
        p_col = self.image.get_at(self.pos_in_image(pos))
        if not (p_col[0] < 70 and p_col[1] > 130 and p_col[2] < 70): return True
        else: return False
        
    def isFinished(self, car_bound):
        top_left = car_bound["top_left"]
        top_right = car_bound["top_right"]
        p_pos = ((top_left[0] + top_right[0])//2, (top_left[1] + top_right[1])//2)
        p_col = self.image.get_at(self.pos_in_image(p_pos))
        if all((e < 10) for e in p_col[:3]): return True
        else: return False
    