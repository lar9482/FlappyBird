import pygame
import sys

from entities.bird import bird
from entities.pipes import pipes
# define some colors in the RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    # set up pygame and its screen
    pygame.init()
    screen_size = (500, 700)
    screen = pygame.display.set_mode(screen_size)

    # create a game clock
    clock = pygame.time.Clock()

    #Flappy bird prototype
    flappy = bird(screen_size)

    #Pipes prototype
    Pipes = pipes(screen_size, flappy.hitbox.height, flappy.hitbox.width)

    while True:
        # handle mouse and keyboard event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            #Event for handling when the spacebar is pressed
            if event.type == 771:
                flappy.jump()

        # fills screen with a background color
        screen.fill(WHITE)

        #Drawing the bird
        flappy.draw(screen)
        
        #Updating the position of the bird
        flappy.update_position()

        #Drawing the pipes
        Pipes.draw(screen)

        Pipes.update_position()

        # update display based on what's drawn on the screen
        pygame.display.flip()
        
        # loop through at most 60 times per second
        clock.tick(60)

main()