from sortedcontainers import SortedList
from ai.node import node, Type
from ai.connection import connection
import random

class genome:
    def __init__(self, num_inputs, num_outputs):

        #Number of input and output nodes in this genome
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

        #The pool of node genes and connection genes
        #They are sorted based on the node IDs/innovation numbers
        self.node_genes = SortedList()
        self.connection_genes = SortedList()

        #Node ID counter for this genome.
        self.curr_node_id = 0
        
        #Insert all input/output nodes into node gene pool
        self.__init_node_genes(num_inputs, num_outputs)

    def __init_node_genes(self, num_inputs, num_outputs):

        #Given the number of inputs, add input nodes with unique node ids
        for i in range(0, num_inputs):
            self.node_genes.add(node(Type.Input, i))
            self.curr_node_id += 1

        #Given the number of output, add output nodes with unique node ids
        for i in range(self.curr_node_id, self.curr_node_id+num_outputs):
            self.node_genes.add(node(Type.Output, i))
            self.curr_node_id += 1

    def init_connection_genes(self, NEAT_Pool):
        chosen_input_id = random.choice(list(range(0, self.num_inputs)))
        chosen_output_id = random.choice(list(range(self.num_inputs, self.num_inputs+self.num_outputs)))

        new_connection_gene = connection(chosen_input_id,
                                         random.uniform(0, 1),
                                         chosen_output_id,
                                         NEAT_Pool.curr_innovation_num)
        
        self.connection_genes.add(new_connection_gene)
        NEAT_Pool.curr_innovation_num += 1
        

    
        