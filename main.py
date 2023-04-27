import pygame
import sys

from entities.bird import bird
from entities.pipes import pipes

class game:
    def __init__(self, screen_size, fps):
        self.screen_size = screen_size

        self.bird = bird(screen_size)
        self.pipes = [pipes(screen_size, self.bird.hitbox.height, self.bird.hitbox.width)]
        self.screen = pygame.display.set_mode(screen_size)

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.fps = fps

    def __has_collided(self, bird, pipe):
        collided = False

        #Case when the bird hits the top pipe
        #First check if the bird's top is positioned higher than the top pipe's bottom
        if (bird.hitbox.top < pipe.top_pipe.bottom):
            #If the bird is entirely left of the top pipe
            leftward = (bird.hitbox.topright[0] < pipe.top_pipe.bottomleft[0] and
                        bird.hitbox.topleft[0] < pipe.top_pipe.bottomleft[0])
            
            #If the bird is entirely right of the top pipe
            rightward = (bird.hitbox.topright[0] > pipe.top_pipe.bottomright[0] and
                        bird.hitbox.topleft[0] > pipe.top_pipe.bottomright[0])
            
            #If neither are true, a colllison has happened
            if (not leftward and not rightward):
                collided = True

        #Case when the bird hits the bottom pipe 
        #First check if the bird's bottom is positioned lowerer than the bottom pipe's top
        if (bird.hitbox.bottom > pipe.bottom_pipe.top):
            
            #If the bird is entirely left of the bottom pipe
            leftward = (bird.hitbox.bottomright[0] < pipe.bottom_pipe.topleft[0] and
                        bird.hitbox.bottomleft[0] < pipe.bottom_pipe.topleft[0])
            
            #If the bird is entirely right of the bottom pipe
            rightward = (bird.hitbox.bottomright[0] > pipe.bottom_pipe.topright[0] and
                        bird.hitbox.bottomleft[0] > pipe.bottom_pipe.topright[0])
            
            #If neither are true, a colllison has happened
            if (not leftward and not rightward):
                collided = True

        return collided
        

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

            self.__has_collided(self.bird, self.pipes[0])

            # fills screen with a background color
            self.screen.fill(self.WHITE)

            #Drawing the bird
            self.bird.draw(self.screen)
        
            #Updating the position of the bird
            self.bird.update_position()

            #For all pipes in the game currently
            for pipe in self.pipes:

                #Draw and update positions of the pipes
                pipe.draw(self.screen)
                pipe.update_position()

            # update display based on what's drawn on the screen
            pygame.display.flip()
        
            # loop through at the fps rate
            clock.tick(self.fps)

    def run_game(self):
        self.__init()
        self.__main_loop()

def main():

    screen_size = (500, 700)
    fps = 60
    Game = game(screen_size, fps)
    Game.run_game()

if __name__ == "__main__":
    main()