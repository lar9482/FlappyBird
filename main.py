import pygame
import sys

from entities.bird import bird
from entities.pipes import pipes

class game:
    def __init__(self, screen_size):
        self.screen_size = screen_size

        self.bird = bird(screen_size)
        self.pipes = [pipes(screen_size, self.bird.hitbox.height, self.bird.hitbox.width)]
        self.screen = pygame.display.set_mode(screen_size)

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

    def __init(self):
        pygame.init()

    def __main_loop(self):
        # create a game clock
        clock = pygame.time.Clock()

        while True:

            # handle mouse and keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
                #Event for handling when the spacebar is pressed
                if event.type == 771:
                    self.bird.jump()
            
            #Remove the first pipe once it removes off screen
            if (self.pipes[0].x <= -self.pipes[0].width_constant*self.pipes[0].bird_width):
                self.pipes.pop(0)
            
            #Adding a pipe to the screen
            if (self.pipes[0].x == self.bird.x):
                self.pipes.append(pipes(self.screen_size, self.bird.hitbox.height, self.bird.hitbox.width))

            # fills screen with a background color
            self.screen.fill(self.WHITE)

            #Drawing the bird
            self.bird.draw(self.screen)
        
            #Updating the position of the bird
            self.bird.update_position()

            #For all pipes in the game currently
            for pipe in self.pipes:

                #Drawing the pipes
                pipe.draw(self.screen)

                #Updating the position of the pipes
                pipe.update_position()

            # update display based on what's drawn on the screen
            pygame.display.flip()
        
            # loop through at most 60 times per second
            clock.tick(60)

    def run_game(self):
        self.__init()
        self.__main_loop()

def main():

    screen_size = (500, 700)
    Game = game(screen_size)
    Game.run_game()

if __name__ == "__main__":
    main()