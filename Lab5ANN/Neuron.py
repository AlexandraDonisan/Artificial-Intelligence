from random import *
from math import *
import numpy as np


class Neuron:
    def __init__(self, numberOfInputs):
        self.numberOfInputs = numberOfInputs
        self.weights = [(random() * 2 - 1) for _ in range(self.numberOfInputs)]
        self.output = 0
        self.error = 0

    def activate(self, info):
        # info = the output of a neuron from a given level
        net = 0.0
        for index in range(self.numberOfInputs):
            net += info[index] * self.weights[index]
        # self.output = net  # linear activation
        self.output = self.sigmoid(net)
        # self.output = 1 / (1.0 + exp(-net));	# for sigmoidal activation

    def setError(self, value):
        self.error = value  # linear activation
        # a formula for sigmoidal activation

    # the activation function:
    def sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))

    # the derivate of the activation function
    def sigmoid_derivative(self, x):
        return x * (1.0 - x)


