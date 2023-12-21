import pygame
from src.game_objects.map import Map
from src.game_objects.car import Car
from config.game_config import *
import neat

class GameManager:

    def __init__(self, screen: pygame.Surface, amount: int = 1):
        self.screen = screen
        self.screen_size = screen.get_size()

        # Setup the game
        self.start_pos_dict = {"01": (-3900, -1200),}

        # Create game objects
        self.maps = []
        self.cars = []
        for i in range(0, amount):
            # create map object
            map = Map(self.screen) # Using map.loadImage(map_id) to load map, default map01
            self.maps.append(map)
            car = Car(self.screen) # Using car.loadImage(car_id) to load car, default car001
            car.velocity = GAME_SPEED
            self.cars.append(car)
        # Data for game handling

    def update(self, nets):
        # train
        for i, map in enumerate(self.maps):
            output = nets[i].activate(self.cars[i].get_data())
            choice = output.index(max(output))
            if choice == 0:
                self.cars[i].angle += ANGLE_UNIT
            elif choice == 1:
                self.cars[i].angle -= ANGLE_UNIT

            # Update map object
            map.update(self.cars[i])

            # Update car object
            self.cars[i].update(map)
            if not self.cars[i].is_alive:
                del self.cars[i]
        
                return False
            return True

 