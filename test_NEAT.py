from ai.genome import genome
from ai.node import node, Type
from ai.connection import connection

from ai.NEAT_Pool import NEAT_Pool

pool = NEAT_Pool(3, 1, 2)
test = pool.population[0]

print()