from Neuron import Neuron


class Layer:
    def __init__(self, numberOfNeurons=0, numberOfInputs=0):
        self.numberOfNeurons = numberOfNeurons  # number of neurons in the layer
        self.neurons = [Neuron(numberOfInputs) for _ in range(self.numberOfNeurons)]

