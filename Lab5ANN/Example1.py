'''
An example of a simple ANN with 1+2 layers
The implementation uses 2 matrixes in order to memorise the weights.

This is a VERY PARTICULAR network with 3 entries and one output.

For a full description:

https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6

'''

import numpy as np
import matplotlib.pyplot as mpl


# the activation function:
def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


# the derivate of te activation function
def sigmoid_derivative(x):
    return x * (1.0 - x)


class NeuralNetwork:
    # constructor for this VERY particular network with 2 layers (plus one for input)

    def __init__(self, x, y):
        self.input = x
        # self.weights1 = np.random.rand(self.input.shape[1], 4)
        # self.weights2 = np.random.rand(4, 1)
        self.weights1 = np.random.rand(self.input.shape[1], self.input.shape[0])
        self.weights2 = np.random.rand(y.shape[0], y.shape[1])
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.loss = []

    # the function that computs the output of the network for some input
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        x = np.dot(self.layer1, self.weights2)
        self.output = sigmoid(x)
        # self.output = sigmoid(np.dot(self.layer1, self.weights2))

    # the backpropagation algorithm
    def backprop(self):
        # application of the chain rule to find derivative of the
        # loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2 * (self.y - self.output) *
                                            sigmoid_derivative(self.output)))

        d_weights1 = np.dot(self.input.T, (np.dot(2 * (self.y - self.output) * sigmoid_derivative(self.output),
                                                  self.weights2.T) * sigmoid_derivative(self.layer1)))
        # update the weights with the derivative (slope) of the loss function

        self.weights1 += d_weights1
        self.weights2 += d_weights2
        diff = self.y - self.output
        d = diff**2
        suma = sum(diff**2)
        self.loss.append(sum((self.y - self.output) ** 2))


def readFromFile():
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


def normalizeData(inputs):
    final = []
    for i in range(len(inputs)):
        aux = []
        mini = min(inputs[i])
        maxi = max(inputs[i])
        for el in inputs[i]:
            new = (el - mini) / (maxi - mini)
            aux.append(new)
        final.append(aux)
    return final


if __name__ == "__main__":
    # X the array of inputs, y the array of outputs, 4 pairs in total
    inputs, outputs = readFromFile()

    # X = np.array(normalizeData(inputs))
    # y = np.array(outputs)
    # print(len(y))
    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])
    y = np.array([[0], [1], [1], [0]])
    nn = NeuralNetwork(X, y)

    nn.loss = []
    iterations = []
    for i in range(1500):
        nn.feedforward()
        nn.backprop()
        iterations.append(i)

    print(nn.output)

    mpl.plot(iterations, nn.loss, label='loss value vs iteration')
    mpl.xlabel('Iterations')
    mpl.ylabel('loss function')
    mpl.legend()
    mpl.show()
