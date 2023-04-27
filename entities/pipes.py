import pygame as pg
import random
class pipes:

    def __init__(self, screen_size, bird_width, bird_height):

        #How wide the pipes are relative to the width of the bird.
        width_constant = 1.5

        #How far apart the pipes are relative to the height of the bird
        height_constant = 3.25

        #Define the "top" and "bottom of the gap between the pipes"
        #The gap 'size' is height_constant*bird_height
        gap_begin = random.uniform(0, screen_size[1]-height_constant*bird_height)
        gap_end = gap_begin + height_constant*bird_height

        self.top_pipe = pg.Rect(screen_size[0]-50, 0, width_constant*bird_width, gap_begin)
        self.bottom_pipe = pg.Rect(screen_size[0]-50, gap_end, width_constant*bird_width, screen_size[1]-gap_end)