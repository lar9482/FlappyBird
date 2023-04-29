from ai.genome import genome

class NEAT_Pool:
    
    #Global innovation number counter
    curr_innovation_num = 0

    def __init__(self, num_inputs, 
                       num_outputs,
                       population_size):

        self.population = []

        for i in range(0, population_size):
            new_genome = genome(num_inputs, num_outputs)
            new_genome.init_connection_genes(self)

            self.population.append(
                new_genome
            )
        
