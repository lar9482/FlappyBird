from ai.genome import genome
from ai.node import node, Type
from ai.connection import connection

from ai.NEAT_Pool import NEAT_Pool

import numpy as np

num_input_nodes = 3
num_output_nodes = 1
population_size = 2


x = np.array([[1, 2, 3], 
              [5, 6, 7]], np.int32)

pool = NEAT_Pool(3, 1, 2)
pool.predict(x)


print()