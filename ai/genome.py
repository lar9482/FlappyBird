from sortedcontainers import SortedList
from ai.node import node, Type
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
        
        self.__init_node_genes(num_inputs, num_outputs)

    def __init_node_genes(self, num_inputs, num_outputs):
        for i in range(0, num_inputs):
            self.node_genes.add(node(Type.Input, i))
            self.curr_node_id += 1

        for i in range(self.curr_node_id, self.curr_node_id+num_outputs):
            self.node_genes.add(node(Type.Output, i))
            self.curr_node_id += 1

    def init_connection_genes(self, innovation_number):
        pass

    
        