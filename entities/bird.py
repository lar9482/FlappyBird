import pygame as pg


class bird:
    def __init__(self, screen_size):

        #Image of the bird, adjusted for the size of the screen
        self.image = pg.transform.scale(
                        pg.image.load('assets/bird1.png'), 
                        (0.1 * screen_size[0], 0.05 * screen_size[1])
                    )

        #Physics constants(v_0, g, and delta_time)
        self.initial_y_velocity = -35
        self.delta_time = 0.20
        self.gravity_constant = 9.81

        #Velocity of the bird(speed of the bird moving vertically)
        self.y_velocity = self.initial_y_velocity

        #Position of the bird
        self.x = 0.25 * screen_size[0]
        self.y = 0.25 * screen_size[1]

    #Calculating y= -(1/2)g^2 + v_y*delta_time + y
    def update_position(self):
        self.y += self.y_velocity * self.delta_time
        self.y_velocity += self.gravity_constant * self.delta_time

    #For a jump, the vertically velocity is set back to the original velocity constant
    def jump(self):
        self.y_velocity = self.initial_y_velocity