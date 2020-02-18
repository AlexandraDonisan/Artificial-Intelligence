from random import *

class Neuron:
    def __init__(self, inputNo):
        self.inputNo = inputNo
        self.weights = [(random() * 2 - 1) for k in range(self.inputNo)]
        self.output = 0