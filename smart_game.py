import pygame
import sys

from entities.bird import bird
from entities.pipes import pipes

from smart_entities.smart_bird import smart_bird
from smart_entities.smart_bird_pool import smart_bird_pool

class smart_game:
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
    
    def __hit_bottom(self, bird):
        return bird.hitbox.y >= self.screen_size[1]
    
    def __died(self, bird):
        return (self.__has_collided(bird, self.pipes[0]) or self.__hit_bottom(bird))
    
    def __can_jump(self, bird):
        return bird.hitbox.y >=0
    
    def __init(self):
        pygame.init()

    def __main_loop(self):
        # create a game clock
        clock = pygame.time.Clock()

        bird_pool = smart_bird_pool(self.screen_size)
        birds_entities = bird_pool.population

        for bird in birds_entities:
            bird.init_bird_entity(self.screen_size)
            bird.start()

        while True:

            # fills screen with a background color
            self.screen.fill(self.WHITE)

            # handle mouse and keyboard events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Remove the first pipe once it removes off screen
            if (self.pipes[0].x <= -self.pipes[0].width_constant*self.pipes[0].bird_width):
                self.pipes.pop(0)
            
            #Adding a pipe to the screen
            if (self.pipes[0].x == self.bird.x):
                self.pipes.append(pipes(self.screen_size, self.bird.hitbox.height, self.bird.hitbox.width))

            birds_updated = 0
            for bird in birds_entities:
                if (bird.end_time == -1):
                    observation = bird.make_observation(self.pipes[0])             
                    jump_or_not = bird.predict(observation)

                    if (jump_or_not > 0.5 and self.__can_jump(bird.bird_entity)):
                        bird.bird_entity.jump()

                    if (self.__died(bird.bird_entity)):
                        bird.end()

                    bird.bird_entity.draw(self.screen)
                    bird.bird_entity.update_position()

                    birds_updated += 1
            
            #For all pipes in the game currently
            for pipe in self.pipes:
                
                #Draw and update positions of the pipes
                pipe.draw(self.screen)
                pipe.update_position()
                
            
            # update display based on what's drawn on the screen
            pygame.display.flip()

            # loop through at the fps rate
            clock.tick(self.fps)

            #Once all of the birds have died(aka, when no birds got updated)
            if (birds_updated == 0):
                
                #Reproduce the birds through the GA
                bird_pool.reproduce()
                
                birds_entities = bird_pool.population

                #Reset the birds
                for bird in birds_entities:
                    bird.reset()
                    bird.init_bird_entity(self.screen_size)
                    bird.start()

                #Reset the pipe
                self.pipes = [pipes(self.screen_size, self.bird.hitbox.height, self.bird.hitbox.width)]

    def run_game(self):
        self.__init()
        self.__main_loop()

def main():
    screen_size = (500, 700)
    fps = 60
    Game = smart_game(screen_size, fps)
    Game.run_game()

if __name__ == "__main__":
    main()