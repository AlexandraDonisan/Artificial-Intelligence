from random import *
from numpy import *
import numpy as np
import matplotlib.pyplot as mpl

def sigmoid(s):
    return 1/(1 + exp(-s))

def derivata(s):
    return s * (1 - s)

class Neuron:
    def __init__(self, inputNo):
        self.inputNo = inputNo
        self.weights = [(random.random() * 2 - 1) for k in range(self.inputNo)]
        self.output = 0


def readFromFile(filename):
    f = open(filename, 'r')
    input = []
    output = []
    for line in f:
        aux = []
        aux.append(float(line.split(",")[0]))
        aux.append(float(line.split(",")[1]))
        aux.append(float(line.split(",")[2]))
        aux.append(float(line.split(",")[3]))
        aux.append(float(line.split(",")[4]))
        aux.append(float(line.split(",")[5]))
        result = line.split(",")[6].split("\n")[0]
        if result == "Hernia":
            output.append([1, 0, 0])
        if result == "Spondylolisthesis":
            output.append([0, 1, 0])
        if result == "Normal":
            output.append([0, 0, 1])
        input.append(aux)
    return input, output

def normData(arr):
    mi = min(arr)
    ma = max(arr)
    for i in range(0, len(arr)):
        arr[i] = (arr[i] - mi) / (ma - mi)
    return arr

def classify(o1, o2, o3):
    ma = max(o1, o2, o3)
    if ma == o1:
        return "Hernia"
    if ma == o2:
        return "Spondylolisthesis"
    return "Normal"


class Layer:
    def __init__(self, neuronNo, inputNo):
        self.neuronNo = neuronNo
        self.neurons = [Neuron(inputNo) for k in range(self.neuronNo)]

input, output = readFromFile("data.txt")

iteration = []
for i in range(0, len(input)):
    iteration.append(i)
    layer0Weights = []
    layer0 = Layer(15, 6) 
    for neuron in layer0.neurons:
        layer0Weights.append(neuron.weights)

    layer1Weights = []
    layer1 = Layer(3, 15)
    for neuron in layer1.neurons:
        layer1Weights.append(neuron.weights)
    for j in range(0, 100):

        input[i] = normData(input[i])
        l0 = input[i]

        layer0WeightsT = array(layer0Weights).T
        layer1WeightsT = array(layer1Weights).T

        d0 = dot(input[i], layer0WeightsT)
        l1 = sigmoid(d0)

        d1 = dot(l1, layer1WeightsT)
        l2 = sigmoid(d1)

        l2_error = output[i] - l2
        l2_delta = l2_error * derivata(l2) 

        l1_error = dot(l2_delta, layer1Weights)
        l1_delta = l1_error * derivata(l1)

    
        layer1Weights += dot(l2, l2_delta)
        layer0Weights += dot(l1, l1_delta)


    print(str(i + 1) + ": " + classify(l2_error[0], l2_error[1], l2_error[2]))

mpl.plot(iteration, loss, label='loss value vs iteration')
mpl.xlabel('Iterations')
mpl.ylabel('loss function')
mpl.legend()
mpl.show()
