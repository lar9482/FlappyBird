from NEAT.genome import genome
from entities.bird import bird

from timeit import default_timer as timer

class smart_bird(genome):
    def __init__(self, num_inputs, num_outputs):
        super().__init__(num_inputs, num_outputs)
        
        self.start_time = -1
        self.end_time = -1

    def init_bird_entity(self, screen_size):
        self.bird_entity = bird(screen_size)

    def reset(self):
        self.start_time = -1
        self.end_time = -1

    def start(self):
        self.start_time = timer()
    
    def end(self):
        self.end_time = timer()

    def make_observation(self, pipe):
        pass