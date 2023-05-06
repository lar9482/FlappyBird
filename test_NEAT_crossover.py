from NEAT.genome import genome
from NEAT.components.node import node, Type
from NEAT.components.connection import connection

from NEAT.NEAT_Pool import NEAT_Pool

import numpy as np

#Emulating the genomes in Stanley's crossover example
def first_test():

    num_inputs = 3
    num_outputs = 1
    innovation_number = 1

    #Initializing the genomes
    first_genome = genome(num_inputs, num_outputs)
    second_genome = genome(num_inputs, num_outputs)

    #Adding the nodes
    first_genome.node_genes.add(node(Type.Hidden, first_genome.curr_node_id))
    first_genome.curr_node_id += 1

    second_genome.node_genes.add(node(Type.Hidden, second_genome.curr_node_id))
    second_genome.curr_node_id += 1

    second_genome.node_genes.add(node(Type.Hidden, second_genome.curr_node_id))
    second_genome.curr_node_id += 1

    #Adding connections
    #1st set
    first_genome.connection_genes.add(
        connection(0, 0.5, 3, innovation_number)
    )
    second_genome.connection_genes.add(
        connection(0, 0.5, 3, innovation_number)
    )
    innovation_number+=1

    #2nd set
    first_genome.connection_genes.add(
        connection(1, 0.5, 3, innovation_number)
    )
    first_genome.connection_genes[innovation_number].enabled=False
    second_genome.connection_genes.add(
        connection(1, 0.5, 3, innovation_number)
    )
    second_genome.connection_genes[innovation_number].enabled=False
    innovation_number+=1

    #3rd set
    first_genome.connection_genes.add(
        connection(2, 0.5, 3, innovation_number)
    )
    second_genome.connection_genes.add(
        connection(2, 0.5, 3, innovation_number)
    )
    innovation_number+=1

    #4th set
    first_genome.connection_genes.add(
        connection(1, 0.5, 4, innovation_number)
    )
    second_genome.connection_genes.add(
        connection(1, 0.5, 4, innovation_number)
    )
    innovation_number+=1

    #5th set
    first_genome.connection_genes.add(
        connection(4, 0.5, 3, innovation_number)
    )
    second_genome.connection_genes.add(
        connection(4, 0.5, 3, innovation_number)
    )
    innovation_number+=1

    #6th set
    second_genome.connection_genes.add(
        connection(4, 0.5, 5, innovation_number)
    )
    innovation_number+=1

    #7th set
    second_genome.connection_genes.add(
        connection(5, 0.5, 3, innovation_number)
    )
    innovation_number+=1

    #8th set
    first_genome.connection_genes.add(
        connection(0, 0.5, 4, innovation_number)
    )
    innovation_number+=1

    #9th set
    second_genome.connection_genes.add(
        connection(2, 0.5, 4, innovation_number)
    )
    innovation_number+=1

    #10th set
    second_genome.connection_genes.add(
        connection(0, 0.5, 5, innovation_number)
    )
    innovation_number+=1

    print()




first_test()