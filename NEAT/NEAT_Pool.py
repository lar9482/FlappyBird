from NEAT.genome import genome
from NEAT.components.node import node, Type
from sortedcontainers import SortedList
import numpy as np
import random

class NEAT_Pool:

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

        #Current generation
        self.generation = 0

        #Global innovation number counter
        self.curr_innovation_num = 0

        #Initialize the population pool
        for i in range(0, population_size):
            new_genome = genone_type(num_inputs, num_outputs)
            new_genome.init_connection_genes(self)

            self.population.append(
                new_genome
            )

    def fitness_function(self, genome):
        return 10*self.population.index(genome)+1
    
    def predict(self, X):
        if (X.shape != (self.population_size, self.num_inputs)):
            raise Exception('NEAT_Pool.predict: Make sure shape of X is (pop_size, num_inputs)')
        
        Y = np.empty((self.population_size, self.num_outputs))

        #Getting output for all of the genomes
        for i in range(0, self.population_size):
            Y[i, :] = self.population[i].predict(X[i, :])
        
        return Y
    
    def reproduce(self):
        #Get the fitness values associated with each genome.
        #For easy access, pair fitness values and genomes together(key is fitness, value is genome)
        fitness_genome_pairing = {self.fitness_function(genome): genome for genome in self.population}

        #Sort the pairings based on fitness value
        fitness_genome_pairing = dict(sorted(fitness_genome_pairing.items()))

        raw_fitnesses = list(fitness_genome_pairing.keys())

        #Getting total rank, which is the integer sum formula
        total_fitnesses = sum(raw_fitnesses)
        
        #Adjusting fitness values to fitness/total_fitness for the selection process
        fitness_genome_pairing = {
            (raw_fitness / (total_fitnesses)): fitness_genome_pairing[raw_fitness] 
            for raw_fitness in raw_fitnesses
        }

        new_population_pool = []

        for i in range(0, self.population_size):
            
            (parent1, fitness1) = self.select(fitness_genome_pairing)
            (parent2, fitness2) = self.select(fitness_genome_pairing)

            child = self.crossover(parent1, parent2, fitness1, fitness2)
            pass
    
    def select(self, fitness_genome_pairing):
        fitness_values = list(fitness_genome_pairing.keys())
        min_fitness = min(fitness_values)
        max_fitness = max(fitness_values)

        chance_threshold = random.uniform(min_fitness, max_fitness)
        for fitness in fitness_values:
            if fitness >= chance_threshold:
                return (fitness_genome_pairing[fitness], fitness)

    def crossover(self, genome1, genome2, fitness1, fitness2):

        #Getting disjointed and matching connection genes based on the innovation numbers
        (disjoint_genes_1, disjoint_genes_2, joined_genes) = self.__find_disjoint_match_genes(genome1, genome2)
        new_genome = genome(self.num_inputs, self.num_outputs)

        #Inheriting matching genes
        for joined_gene in joined_genes:
            new_genome.connection_genes.add(random.choice(joined_gene))

        #Inherit disjoint genes based on fitness
        if (fitness2 <= fitness1):
            for disjointed_gene in disjoint_genes_1:
                new_genome.connection_genes.add(disjointed_gene)
        if (fitness1 <= fitness2):
            for disjointed_gene in disjoint_genes_2:
                new_genome.connection_genes.add(disjointed_gene)
        
        curr_node_ids = [gene.id for gene in new_genome.node_genes]

        #Inherit node genes and randomly enable connection genes 25% of the time
        
        #Basically, given every in_node_id and out_node_id in the connection genes,
        #if they don't yet exist in the new genome, create a new node gene for them
        for connection_gene in new_genome.connection_genes:
            if (not connection_gene.in_node_id in curr_node_ids):
                new_genome.node_genes.add(node(Type.Hidden, connection_gene.in_node_id))
                curr_node_ids.append(connection_gene.in_node_id)
            if (not connection_gene.out_node_id in curr_node_ids):
                new_genome.node_genes.add(node(Type.Hidden, connection_gene.out_node_id))
                curr_node_ids.append(connection_gene.out_node_id)

            if (not connection_gene.enabled and random.uniform(0, 1) < 0.25):
                connection_gene.enabled = True
        
        #Adjust the current node id based all of the recently inherited node genes
        new_genome.curr_node_id = max(curr_node_ids)+1

        return new_genome

    def __find_disjoint_match_genes(self, genome1, genome2):
        disjoint_genes_1 = []
        disjoint_genes_2 = []
        joined_genes = []

        i = j = 0
        
        while ((i < len(genome1.connection_genes)) and (j < len(genome2.connection_genes))) :
            if (genome1.connection_genes[i].innovation_number < genome2.connection_genes[j].innovation_number):
                disjoint_genes_1.append(genome1.connection_genes[i])
                i += 1

            elif (genome2.connection_genes[j].innovation_number < genome1.connection_genes[i].innovation_number):
                disjoint_genes_2.append(genome2.connection_genes[j])
                j += 1
            
            elif (genome1.connection_genes[i].innovation_number == genome2.connection_genes[j].innovation_number):
                joined_genes.append((genome1.connection_genes[i], genome2.connection_genes[j]))
                i += 1
                j += 1

        while (i < len(genome1.connection_genes)):
            disjoint_genes_1.append(genome1.connection_genes[i])
            i += 1

        while (j < len(genome2.connection_genes)):
            disjoint_genes_2.append(genome2.connection_genes[j])
            j += 1

        return (disjoint_genes_1, disjoint_genes_2, joined_genes)