from NEAT.NEAT_Pool import NEAT_Pool
from smart_entities.smart_bird import smart_bird

class smart_bird_pool(NEAT_Pool):
    def __init__(
            self, screen_size, 
            num_inputs = 7, 
            num_outputs = 1,
            population_size = 30,
            add_node_rate = 0.4,
            add_connection_rate = 0.4,
            adjust_weight_rate = 0.8,
            num_elites = 5
        ):
        
        genome_type = smart_bird 
        super().__init__(
            num_inputs, 
            num_outputs,
            population_size,
            genome_type,
            add_node_rate,
            add_connection_rate,
            adjust_weight_rate,
            num_elites
        )

        self.screen_size = screen_size

        for bird in self.population:
            bird.init_bird_entity(screen_size)

    def fitness_function(self, bird):
        return (bird.end_time - bird.start_time) + (50/bird.distance)
