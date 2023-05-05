from NEAT.genome import genome
import numpy as np

class NEAT_Pool:

    #Global innovation number counter
    curr_innovation_num = 0

    def __init__(self, num_inputs, 
                       num_outputs,
                       population_size,
                       genone_type = genome):

        #The population pool itself of genome objects
        self.population = []

        self.population_size = population_size

        #Number of input and output nodes in this pool
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

        self.generation = 0

        #Initialize the population pool
        for i in range(0, population_size):
            new_genome = genone_type(num_inputs, num_outputs)
            new_genome.init_connection_genes(self)

            self.population.append(
                new_genome
            )

    def fitness_function(self, genome):
        return self.population.index(genome)
    
    def predict(self, X):
        if (X.shape != (self.population_size, self.num_inputs)):
            raise Exception('NEAT_Pool.predict: Make sure shape of X is (pop_size, num_inputs)')
        
        Y = np.empty((self.population_size, self.num_outputs))

        #Getting output for all of the genomes
        for i in range(0, self.population_size):
            Y[i, :] = self.population[i].predict(X[i, :])
        
        return Y
    
    def reproduce(self):
        pass