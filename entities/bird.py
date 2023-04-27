import pygame as pg

class bird:
    def __init__(self, screen_size):

        #Position of the bird
        self.x = 0.25 * screen_size[0]
        self.y = 0.25 * screen_size[1]

        #Image of the bird, adjusted for the size of the screen
        self.image = pg.transform.scale(
                        pg.image.load('assets/bird1.png'), 
                        (0.1 * screen_size[0], 0.05 * screen_size[1])
                    )

        self.y_velocity = -35
        self.delta_time = 0.20

    def update_position(self):
        self.y += self.y_velocity * self.delta_time
        self.y_velocity += 9.81 * self.delta_time

    def jump(self):
        self.y_velocity = -35