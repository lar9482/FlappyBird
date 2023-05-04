from ai.genome import genome
from ai.node import node, Type
from ai.connection import connection

from ai.NEAT_Pool import NEAT_Pool

import numpy as np

num_input_nodes = 3
num_output_nodes = 1
population_size = 2

# (population_size, num_inputs)
x = np.array([[1, 2, 3], 
              [5, 6, 7]], np.int32)

pool = NEAT_Pool(
    num_input_nodes, 
    num_output_nodes, 
    population_size
)

y = pool.predict(x)
print(x)
print(y)