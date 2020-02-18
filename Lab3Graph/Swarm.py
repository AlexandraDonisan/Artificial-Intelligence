from random import randint

from Particle import Particle


class Swarm:
    def __init__(self, numberOfParticles, sizeOfParticle):
        self.numberOfParticles = numberOfParticles
        self.sizeOfParticle = sizeOfParticle
        self.particles = self.population()  # list of particles

    def population(self):
        return [Particle(self.sizeOfParticle) for x in range(self.numberOfParticles)]

    def selectNeighbors(self, pop, nSize):
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

    def getBestNeighbour(self, particle):
        pass

    def getBestParticles(self):  # list of particles
        pass