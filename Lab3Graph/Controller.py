from random import random

import math

from Problem import Problem
from Swarm import Swarm
import matplotlib.pyplot as plt


class Controller:
    def __init__(self):
        self.population = None  # population:swarm

    def iteration(self, pop, neighbors, c1, c2, w):
        bestNeighbors = []
        # determine the best neighbor for each particle
        for i in range(len(pop)):
            bestNeighbors.append(neighbors[i][0])
            for j in range(1, len(neighbors[i])):
                if pop[bestNeighbors[i]].getFitness() > pop[neighbors[i][j]].getFitness():
                    bestNeighbors[i] = neighbors[i][j]

        # update the velocity for each particle
        for i in range(len(pop)):
            for j in range(len(pop[0].velocity)):
                newVelocity = w * pop[i].velocity[j]
                newVelocity = newVelocity + c1 * random() * (pop[bestNeighbors[i]].getPosition()[j] - pop[i].getPosition()[j])
                newVelocity = newVelocity + c2 * random() * (pop[i].getBestPosition()[j] - pop[i].getPosition()[j])
                pop[i].velocity[j] = newVelocity

        # update the position for each particle
        for i in range(len(pop)):
            newPosition = []
            for j in range(len(pop[0].velocity)):
                x = self.sigmoid(pop[i].velocity[j])
                if x <= 0.5:
                    newPosition.append(0)
                else:
                    newPosition.append(1)
            count1s = 0
            for el in newPosition:
                if el == 1:
                    count1s += 1
            if count1s == pop[0].getSizeOfParticle()/2:
                #pop[i]._position = newPosition
                pop[i].setPosition(newPosition)
                pop[i].evaluate()
                pop[i].update()
        return pop

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def runAlgorithm(self):  # list of particles
        filename = "in.txt"
        p = Problem(filename)
        graph, vertices = p.readFromFile()
        # PARAMETERS:
        noIteratii = 100
        # number of particles
        noParticles = 100
        # individual size
        dimParticle = len(graph)
        # specific parameters for PSO
        w = 1.0
        c1 = 1.0
        c2 = 2.5
        sizeOfNeighborhood = 20

        swarm = Swarm(noParticles, dimParticle)
        P = swarm.population()
        self.population = p

        # we establish the particles' neighbors
        neighborhoods = swarm.selectNeighbors(P, sizeOfNeighborhood)

        avgfitness = []
        for i in range(noIteratii):
            P = self.iteration(P, neighborhoods, c1, c2, w / (i + 1))
            avgfitness.append(self.getAverage(P))

        best = 0
        for i in range(1, len(P)):
            if P[i].getFitness() < P[best].getFitness():
                best = i

        fitnessOptim = P[best].getFitness()
        individualOptim = P[best].getPosition()

        print("fitnessOptim " + str(fitnessOptim))
        print("individualOptim " + str(individualOptim))
        self.getPlot(avgfitness)

    def getAllFitnesses(self):
        return [particle.getFitness() for particle in self.population]

    def statistics(self):
        fitnesses = self.getAllFitnesses()
        sumFitnesses = 0
        for el in fitnesses:
            sumFitnesses += el
        meanValue = sumFitnesses / int(len(fitnesses))

        stdSum = 0
        for el in fitnesses:
            stdSum = math.pow(el - meanValue, 2)
        standardDeviation = math.sqrt(stdSum / (len(fitnesses) - 1))

        return meanValue, standardDeviation

    def getPlot(self, avgfitness):
        plt.plot(avgfitness)
        # plt.ylabel('some numbers')
        plt.show()

    def getAverage(self, population):
        sum = 0
        size = len(population)
        for el in population:
            sum += el.getFitness()
        return sum / size


def main():
    filename = "in.txt"
    p = Problem(filename)
    graph, vertices = p.readFromFile()
    print("graph: "+str(graph))
    print("vertices: "+ str(vertices))
    ctrl = Controller()
    ctrl.runAlgorithm()


main()
