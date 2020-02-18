from Neuron import Neuron


class Layer:
    def __init__(self, neuronNo, inputNo):
        self.neuronNo = neuronNo
        self.neurons = [Neuron(inputNo) for k in range(self.neuronNo)]