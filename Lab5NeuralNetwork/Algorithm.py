from numpy import *
import matplotlib.pyplot as mpl

from Layer import Layer


class Algorithm:
    def __init__(self):
        pass

    def sigmoid(self, s):
        return 1 / (1 + exp(-s))

    def sigmoid_derivative(self, s):
        return s * (1 - s)

    def readFromFile(self, filename):
        file = open(filename)
        lines = file.read().split("\n")
        inputs = []
        outputs = []
        for i in range(len(lines)):
            aux = []
            l = lines[i].split(",")
            for el in l:
                if el == 'Hernia':
                    outputs.append([1, 0, 0])
                elif el == 'Spondylolisthesis':
                    outputs.append([0, 1, 0])
                elif el == 'Normal':
                    outputs.append([0, 0, 1])
                else:
                    aux.append(float(el))
            inputs.append(aux)
        return inputs, outputs

    def normalizeData(self, arr):
        mini = min(arr)
        maxi = max(arr)
        for i in range(0, len(arr)):
            arr[i] = (arr[i] - mini) / (maxi - mini)
        return arr

    def decode(self, output1, output12, output3):
        maxi = max(output1, output12, output3)
        if maxi == output1:
            return "Hernia"
        if maxi == output12:
            return "Spondylolisthesis"
        return "Normal"

    def getMax(self, arr):
        res = []
        for el in arr:
            res.append(max(el))
        return res

    def run2(self):
        input, output = self.readFromFile("data.txt")
        final_loss = []
        loss_x = []
        iteration = []

        # initialize nn
        layer0Weights = []
        layer0 = Layer(15, 6)
        for neuron in layer0.neurons:
            layer0Weights.append(neuron.weights)

        layer1Weights = []
        layer1 = Layer(3, 15)
        for neuron in layer1.neurons:
            layer1Weights.append(neuron.weights)

        for j in range(0, 100):
            iteration.append(j)

            for i in range(0, len(input)):
                    input[i] = self.normalizeData(input[i])

                    layer0WeightsT = array(layer0Weights).T
                    layer1WeightsT = array(layer1Weights).T

                    d0 = dot(input[i], layer0WeightsT)
                    l1 = self.sigmoid(d0)

                    d1 = dot(l1, layer1WeightsT)
                    l2 = self.sigmoid(d1)

                    l2_error = output[i] - l2
                    l2_delta = l2_error * self.sigmoid_derivative(l2)

                    l1_error = dot(l2_delta, layer1Weights)
                    l1_delta = l1_error * self.sigmoid_derivative(l1)

                    layer1Weights += dot(l2, l2_delta)
                    layer0Weights += dot(l1, l1_delta)

                    if j % 100 == 99:
                        x = output[i] - l2_error
                        loss_x.append(sum(x**2))
                        # print("Diagnosis " + str(j + 1) + ": " + self.decode(l2_error[0], l2_error[1], l2_error[2]) + "err: [ " + str(l2_error[0]) + str(l2_error[1]) + str(l2_error[2]) + "]" + " sum= " + str(loss_x[-1]))
                        print(
                            "Diagnosis " + str(j + 1) + ": " + self.decode(l2_error[0], l2_error[1], l2_error[2]) + " err: [ " + str(
                                l2_error[0]) + " " + str(l2_error[1]) + " " + str(l2_error[2]) + "]") # + " sum= " + str(loss_x[-1]))

            final_loss.append(sum((output[i] - l2_error)**2))

        mpl.plot(iteration, final_loss, label='loss value vs iteration')
        mpl.xlabel('Iterations')
        mpl.ylabel('loss function')
        mpl.legend()
        mpl.show()


def start():
    a = Algorithm()
    a.run2()


start()


# def run(self):
#     input, output = self.readFromFile("data.txt")
#     loss = []
#     loss_x = []
#     iteration = []
#     for i in range(0, len(input)):
#         iteration.append(i)
#         layer0Weights = []
#         layer0 = Layer(15, 6)
#         for neuron in layer0.neurons:
#             layer0Weights.append(neuron.weights)
#
#         layer1Weights = []
#         layer1 = Layer(3, 15)
#         for neuron in layer1.neurons:
#             layer1Weights.append(neuron.weights)
#         for j in range(0, 100):
#             input[i] = self.normalizeData(input[i])
#
#             layer0WeightsT = array(layer0Weights).T
#             layer1WeightsT = array(layer1Weights).T
#
#             d0 = dot(input[i], layer0WeightsT)
#             l1 = self.sigmoid(d0)
#
#             d1 = dot(l1, layer1WeightsT)
#             l2 = self.sigmoid(d1)
#
#             l2_error = output[i] - l2
#             l2_delta = l2_error * self.sigmoid_derivative(l2)
#
#             l1_error = dot(l2_delta, layer1Weights)
#             l1_delta = l1_error * self.sigmoid_derivative(l1)
#
#             layer1Weights += dot(l2, l2_delta)
#             layer0Weights += dot(l1, l1_delta)
#             # if j == 99:
#             #     err =[]
#             #     err.append()
#
#         x = l2_error
#         loss_x.append(sum(x ** 2))
#         # loss.append(sum(l2_error ** 2))
#         loss1 = []
#         # loss1 = self.getMax(loss_x)
#
#         print("Diagnosis " + str(i + 1) + ": " + self.decode(l2_error[0], l2_error[1], l2_error[2]) + "err: [ " + str(
#             l2_error[0]) + str(l2_error[1]) + str(l2_error[2]))
#
#     y = loss_x
#     mpl.plot(iteration, sorted(loss_x, reverse=True), label='loss value vs iteration')
#     mpl.xlabel('Iterations')
#     mpl.ylabel('loss function')
#     mpl.legend()
#     mpl.show()
