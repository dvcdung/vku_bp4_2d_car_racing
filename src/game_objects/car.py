import pygame
import numpy as np
from config.game_config import *
from src.utils.image_handler import ImageHandler as imgHander

class Car:
    def __init__(self, screen: pygame.Surface):
        self.folder_path = "assets/cars/"
        self.screen = screen
        # car properties
        self.id = None
        self.image = None
        self.size = CAR_SIZE
        self.is_alive = True
        self.is_finished = False
        # location properties
        self.center_pos = (screen.get_size()[0] // 2, screen.get_size()[1] // 2)
        self.angle = 90
        self.rect = None
        # physical properties
        self.velocity = 0
        self.radars = []
        self.distance = 0
        # initialization
        self.loadImage()

    # for game update
    def update(self, map):
        if self.is_alive: 
            # car update
            image_rotated, rect = imgHander.rotate(self.image, self.angle - 90, self.center_pos)
            self.rect = rect
            self.distance += self.velocity
            # handle collision
            self.handle_collision(map)
            # draw to screens
            self.scan_radars(map)
        else:
            self.set_stop()

    def draw(self, top_left=None):
        image_rotated, rect = imgHander.rotate(self.image, self.angle - 90, self.center_pos)
        self.screen.blit(image_rotated, self.rect.topleft if not top_left else top_left)

    def bound(self):
        alpha = self.angle*np.pi/180
        delta_angle = np.arctan(self.size[0]/self.size[1])
        hypotenuse = np.sqrt((self.size[0]//2)**2 + (self.size[1]//2)**2)
        return {"top_left": (self.center_pos[0] + hypotenuse * np.cos(alpha + delta_angle), self.center_pos[1] - hypotenuse * np.sin(alpha + delta_angle)),
                "bottom_left": (self.center_pos[0] + hypotenuse * np.cos(alpha + np.pi - delta_angle), self.center_pos[1] - hypotenuse * np.sin(alpha + np.pi - delta_angle)),
                "bottom_right": (self.center_pos[0] + hypotenuse * np.cos(alpha + np.pi + delta_angle), self.center_pos[1] - hypotenuse * np.sin(alpha + np.pi + delta_angle)),
                "top_right": (self.center_pos[0] + hypotenuse * np.cos(alpha + 2*np.pi - delta_angle), self.center_pos[1] - hypotenuse * np.sin(alpha + 2*np.pi - delta_angle))}

    def loadImage(self, car_id="001"):
        self.id = car_id
        self.image = imgHander.load(f"{self.folder_path}car{self.id}.png", self.size)

    # scan radars
    def scan_radars(self, map):
        self.radars = []
        for degree in range(-90, 91, 45):
            degree += self.angle
            # code lines to determine position of radar in border
            length = 0 # length of radar, not distance
            radar_pos = self.center_pos
            while map.isInTrack(radar_pos):
                length += 1
                radar_pos = (int(self.center_pos[0] + length*np.cos(degree * np.pi / 180)), 
                            int(self.center_pos[1] - length*np.sin(degree * np.pi / 180)))
            # distance from center to border according to radar line
            distance = int(np.sqrt((radar_pos[0] - self.center_pos[0])**2 + (radar_pos[1] - self.center_pos[1])**2))
            # add radar to self.radars
            self.radars.append([radar_pos, distance])
    
    def draw_radars(self):
        # draw radar
        for radar_pos, distance in self.radars:
            pygame.draw.line(self.screen, J_RED, self.center_pos, radar_pos, 2)
            pygame.draw.circle(self.screen, J_RED, radar_pos, 3)
  
    def get_data(self):
        return_values = [0, 0, 0, 0, 0]
        for i, r in enumerate(self.radars):
            return_values[i] = int(r[1]/30)
        return return_values

    # on listen for keyboard events
    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += ANGLE_UNIT
        if keys[pygame.K_RIGHT]:
            self.angle -= ANGLE_UNIT
        if keys[pygame.K_SPACE]:
            self.velocity = GAME_SPEED

    # handle collision events
    def handle_collision(self, map):
        car_bound = self.bound()
        if map.isFinished(car_bound):
            print("Your car has completed the race!")
            self.is_alive = False
            self.is_finished = True
        else:
            for point in car_bound.values():
                if not map.isInTrack(point):
                    # print("Your car is dead!")
                    self.is_alive = False

    # set car stop 
    def set_stop(self):
        self.velocity = 0
