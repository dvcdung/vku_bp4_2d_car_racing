import pygame
from src.game_objects.map import Map
from src.game_objects.car import Car

class GameManager:

    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.screen_size = screen.get_size()

        # Setup the game
        self.start_pos_dict = {"01": (-3900, -1400),}

        # Create game objects
        self.map = Map(self.screen) # Using map.loadImage(map_id) to load map, default map01
        self.car = Car(self.screen) # Using car.loadImage(car_id) to load car, default car001

        # Data for game handling
        self.car_bounds = {}

    def update(self):
        # handle keyboard events
        self.car.handle_events()
        # print(self.map.image.get_at(self.map.pos_in_image(pygame.mouse.get_pos())))

        # Update map object
        self.map.move(self.car.velocity, self.car.angle)
        self.map.update()

        # Update car object
        self.car.update()

        # handle collision events
        self.car_bounds[self.car.id] = self.car.bound()
        for car_bound in self.car_bounds.values():
            for point in car_bound.values():
                if not self.map.isInTrack(point):
                    if self.map.isFinished(point):
                        print("Your car has completed the race!")
                    else:
                        print("Your car is dead!")
                        self.car.is_alive = False

 