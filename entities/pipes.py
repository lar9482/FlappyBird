import pygame as pg
import random

class pipes:
    def __init__(self, screen_size, bird_width, bird_height):
        #How much x should change when the pipes move
        self.deltaX = 3

        #How wide the pipes are relative to the width of the bird.
        self.width_constant = 1.5

        #How far apart the pipes are relative to the height of the bird
        self.height_constant = 3.5

        #The horizational position of the pipes
        self.x = screen_size[0]

        #Keep track of the bird's width and height for use later
        self.bird_width = bird_width
        self.bird_height = bird_height

        #Define the "top" and "bottom" of the gap between the pipes
        #The gap 'size' is height_constant*bird_height
        gap_begin = random.uniform(0, screen_size[1]-self.height_constant*self.bird_height)
        gap_end = gap_begin + self.height_constant*self.bird_height

        #Defining the rectangles for the top and bottom pipes.
        self.top_pipe = pg.Rect(self.x, 0, self.width_constant*self.bird_width, gap_begin)
        self.bottom_pipe = pg.Rect(self.x, gap_end, self.width_constant*self.bird_width, screen_size[1]-gap_end)

    #Draw the top and bottom pipes
    def draw(self, screen):
        pg.draw.rect(screen, color='green', rect=self.top_pipe)
        pg.draw.rect(screen, color='green', rect=self.bottom_pipe)

    def update_position(self):
        self.x -= self.deltaX

        self.top_pipe.update(
            self.x,
            self.top_pipe.top,
            self.top_pipe.width,
            self.top_pipe.height
        )

        self.bottom_pipe.update(
            self.x,
            self.bottom_pipe.top,
            self.bottom_pipe.width,
            self.bottom_pipe.height
        )