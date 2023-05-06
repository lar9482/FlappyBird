from NEAT.genome import genome
from entities.bird import bird

class smart_bird(genome):
    def __init__(self, screen_size, num_inputs, num_outputs):

        super().__init__(num_inputs, num_outputs)

        self.bird_entity = bird(screen_size)
        
        self.start_time = -1
        self.end_time = -1