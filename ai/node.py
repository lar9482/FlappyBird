from enum import Enum
import math

class Type(Enum):
    Input = 0
    Hiden = 1
    Output = 2

class node:
    def __init__(self, type = Type.Input, id = 0):
        self.type = type
        self.value = 0
        self.activated_value = 0

        self.id = id

    def feed(self, weight, value):
        self.value += weight*value

    def activate_node(self):
        self.activated_value = self.__sigmoid(self.value)

    def reset_node(self):
        self.value = 0
        self.activated_value = 0

    def __sigmoid(self, value):
        if (value > 50):
            return 0.99999
        elif (value < -50):
            return 0.00001
        else:
            return (math.exp(value)) / (1 + math.exp(value))
        
    #Less than 'operator' for comparison of 'nodes'
    def __lt__(self, other):
        return self.id <= other.id