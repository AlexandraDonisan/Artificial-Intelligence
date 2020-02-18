"""
9. Subgraphs (EA and PSO)
Consider an undirected graph G(V , E) with 2n nodes ( V is the set of nodes, and
E is the set of edges). Partitionate the set of nodes in two disjoint sets V 1 and V 2
, each containing exactly n nodes, in such a way that between any two nodes of the subgraphs
determined by the subsets of nodes should be a path (both subgraphs are conex).
"""
import itertools
from random import randint, random

import math

from Particle import Particle
from Problem import Problem


def population(numberOfParticles, sizeOfParticle):
    return [Particle(sizeOfParticle) for x in range(numberOfParticles)]


def selectNeighbors(pop, nSize):
    if nSize > len(pop):
        nSize = len(pop)
    neighbors = []
    for i in range(len(pop)):
        localNeighbor = []
        for j in range(nSize):
            x = randint(0, len(pop) - 1)
            while x in localNeighbor:
                x = randint(0, len(pop) - 1)
            localNeighbor.append(x)
        neighbors.append(localNeighbor.copy())
    return neighbors


def iteration(pop, neighbors, c1, c2, w):
    """
    an iteration

    pop: the current state of the population


    for each particle we update the velocity and the position
    according to the particle's memory and the best neighbor's pozition
    """
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
            p1 = pop[bestNeighbors[i]].getPosition()[j]
            p2 = pop[i].getPosition()[j]
            p3 = pop[i].getBestPosition()[j]
            p4 = pop[i].getPosition()[j]
            newVelocity = newVelocity + c1 * random() * (
                        pop[bestNeighbors[i]].getPosition()[j] - pop[i].getPosition()[j])
            newVelocity = newVelocity + c2 * random() * (pop[i].getBestPosition()[j] - pop[i].getPosition()[j])
            pop[i].velocity[j] = newVelocity

    # update the pozition for each particle
    for i in range(len(pop)):
        newPozition = []
        for j in range(len(pop[0].velocity)):
            x = sigmoid(pop[i].velocity[j])
            if x <= 0.5:
                newPozition.append(0)
            else:
                newPozition.append(1)

        pop[i]._position = newPozition
        pop[i].evaluate()
        pop[i].update()
    return pop


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def main():
    filename = "in.txt"
    p = Problem(filename)
    graph, vertices = p.readFromFile()
    # PARAMETERS:
    noIteratii = 10
    # number of particles
    noParticles = 10
    # individual size
    dimParticle = len(graph)
    # specific parameters for PSO
    w = 1.0
    c1 = 1.0
    c2 = 2.5
    sizeOfNeighborhood = 3
    P = population(noParticles, dimParticle)

    # we establish the particles' neighbors
    neighborhoods = selectNeighbors(P, sizeOfNeighborhood)

    for i in range(noIteratii):
        P = iteration(P, neighborhoods, c1, c2, w / (i + 1))

    best = 0
    for i in range(1, len(P)):
        if P[i].getFitness() < P[best].getFitness():
            best = i

    fitnessOptim = P[best].getFitness()
    individualOptim = P[best].getPosition()

    print("fitnessOptim " + str(fitnessOptim))
    print("individualOptim " + str(individualOptim))


main()
