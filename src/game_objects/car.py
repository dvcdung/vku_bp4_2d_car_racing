import pygame
import numpy as np
from src.utils.image_handler import ImageHandler as imgHander

class Car:
    def __init__(self, screen: pygame.Surface):
        self.folder_path = "assets/cars/"
        self.screen = screen
        # car properties
        self.id = None
        self.image = None
        self.size = (50, 100)
        self.is_alive = True
        # location properties
        self.center_pos = (screen.get_size()[0] // 2, screen.get_size()[1] // 2)
        self.angle = 90
        self.rect = None
        # physical properties
        self.velocity = 0
        # initialization
        self.loadImage()

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

    # for game update
    def update(self):
        if self.is_alive:
            # car update
            image_rotated, rect = imgHander.rotate(self.image, self.angle - 90, self.center_pos)
            self.rect = rect
            # draw to screen
            self.screen.blit(image_rotated, self.rect.topleft)
    
    # on listen for keyboard events
    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += 3
        if keys[pygame.K_RIGHT]:
            self.angle -= 3
        if keys[pygame.K_SPACE]:
            self.velocity = 15

    