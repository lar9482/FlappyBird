from ai.genome import genome
import numpy as np

class NEAT_Pool:

    #Global innovation number counter
    curr_innovation_num = 0

    def __init__(self, num_inputs, 
                       num_outputs,
                       population_size):

        #The population pool itself of genome objects
        self.population = []

        self.population_size = population_size

        #Number of input and output nodes in this pool
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

        self.generation = 0

        #Initialize the population pool
        for i in range(0, population_size):
            new_genome = genome(num_inputs, num_outputs)
            new_genome.init_connection_genes(self)

            self.population.append(
                new_genome
            )

    def predict(self, X):
        if (X.shape != (self.population_size, self.num_inputs)):
            raise Exception('NEAT_Pool.predict: Make sure shape of X is (pop_size, num_inputs)')
        
        Y = np.empty((self.population_size, self.num_outputs))

        #Getting output for all of the genomes
        for i in range(0, self.population_size):
            curr_X = X[i, :]
            
            Y[i, :] = self.population[i].predict(curr_X)
        
        return Y

