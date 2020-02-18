from Layer import Layer
import numpy as np


class Network:
    def __init__(self, numberOfInputs=0, numberOfOutputs=0, numberOfHiddenLayers=0, numberOfNeuronsPerHiddenLayer=0):
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.numberOfHiddenLayers = numberOfHiddenLayers
        self.numberOfNeuronsPerHiddenLayer = numberOfNeuronsPerHiddenLayer
        self.layers = [Layer(self.numberOfInputs, 0)]  # Input layer
        self.layers += [Layer(self.numberOfNeuronsPerHiddenLayer, self.numberOfInputs)]  # Hidden layer
        # self.layers +=[Layer(self.numberOfNeuronsPerHiddenLayer, self.numberOfNeuronsPerHiddenLayer)
        #                for _ in range(self.numberOfHiddenLayers)]  # Hidden layers
        self.layers += [Layer(self.numberOfOutputs, self.numberOfNeuronsPerHiddenLayer)]  # Output layer

    def activate(self, inputs):
        i = 0

    def normalizeData(self):
        pass

    def feedForward(self):
        l0 = self.layers[0]
        for layer in self.layers[1:]:
            l1 = self.sigmoid(np.dot(l0, ))
        pass

    def backward(self):
        pass

    def sigmoid(self, x):
        return 1.0 / (1 + np.exp(-x))

    # the derivate of the activation function
    def sigmoid_derivative(self, x):
        return x * (1.0 - x)

    def readFromFile(self):
        file = open('file1.txt')
        lines = file.read().split("\n")
        inputs = []
        outputs = []
        for i in range(len(lines)):
            aux = []
            l = lines[i].split(" ")
            for el in l:
                if el == 'NO':
                    outputs.append([1, 0, 0])
                elif el == 'DH':
                    outputs.append([0, 1, 0])
                elif el == 'SL':
                    outputs.append([0, 0, 1])
                else:
                    aux.append(float(el))
            inputs.append(aux)
        return inputs, outputs

    def normalizeData(self, inputs):
        final = []
        for i in range(len(inputs)):
            aux =[]
            mini = min(inputs[i])
            maxi = max(inputs[i])
            for el in inputs[i]:
                new = (el - mini)/(maxi - mini)
                aux.append(new)
            final.append(aux)
        return final

def main():
    y1 = np.array([[0, 0, 1, 1]])
    y = np.array([[0, 0, 1, 1]]).T
    print(y)
    print(y1)
    nn = Network()
    inputs, outputs = nn.readFromFile()
    print(inputs)
    print(outputs)
    print('--------------')
    print(nn.normalizeData(inputs))


main()
