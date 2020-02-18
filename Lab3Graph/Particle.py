import itertools
import operator
import random
from collections import defaultdict
from functools import reduce

from Problem import Problem


class Particle:
    def __init__(self, sizeOfParticle):
        self._initialGraph = Problem("in.txt").getGraph()
        # self._initialVertices = Problem("in.txt").getVertices()
        self._initialDictionary = Problem("in.txt").getDictionary()
        self._sizeOfParticle = sizeOfParticle
        self._position = self.getRandom()
        self._fitness = None
        self.evaluate()
        self.velocity = [0 for x in range(sizeOfParticle)]
        self._bestPosition = self._position.copy()
        self._bestFitness = self._fitness

    def evaluate(self):
        self._fitness = self.fitness(self._position)

    def update(self):
        if self._fitness < self._bestFitness:
            self._bestFitness = self._fitness
            self._bestPosition = self._position

    def fitness(self, position):
        # minimization problem
        # if there is no path between 2 nodes of a subgraph, fitness increases
        f = 0
        g1 = []
        g2 = []
        for el in range(len(position)):
            if position[el] == 0:
                g1.append(self._initialGraph[el])
            else:
                g2.append(self._initialGraph[el])
        v1 = []
        v2 = []
        for el in g1:
            allVertices1 = self._initialDictionary[el]
            l = []
            for i in allVertices1:
                if i in g1:
                    l.append(i)
            v1.append(l)

        for el in g2:
            allVertices1 = self._initialDictionary[el]
            l = []
            for i in allVertices1:
                if i in g2:
                    l.append(i)
            v2.append(l)

        dict1 = self.makeDict(g1, v1)
        dict2 = self.makeDict(g2, v2)

        resBfs1 = self.BFS(dict1, g1[0])
        resBfs2 = self.BFS(dict2, g2[0])

        if len(resBfs1) != len(g1):
            f += 1
        if len(resBfs2) != len(g2):
            f += 1
        return f

    def BFS(self, graph, s):  # graph - dictionary
        result = []
        keyList = list(graph)
        visited = [False] * (len(graph))
        queue = [s]
        indexInVisited = keyList.index(s)
        visited[indexInVisited] = True
        while queue:
            s = queue.pop(0)
            if s not in result:
                result.append(s)
            for i in graph[s]:
                indexInVisited = keyList.index(i)
                if not visited[indexInVisited]:
                    queue.append(i)
                    visited[indexInVisited] = True
        return result

    def allPermutations(self, listA):
        perm = itertools.permutations(listA)
        allPermutations = []
        for i in list(perm):
            allPermutations.append(list(i))
        return allPermutations

    def makeDict(self, graph, vertices):
        G = defaultdict(list)
        for node in range(len(graph)):
            G[graph[node]].append(vertices[node])
        for node in range(len(graph)):
            G[graph[node]] = reduce(operator.concat, G[graph[node]])
        return G

    def getRandom(self):
        randomList = []
        for i in range(self._sizeOfParticle):
            if i < self._sizeOfParticle / 2:
                randomList.append(1)
            else:
                randomList.append(0)
        allPermutations = self.allPermutations(randomList)
        x = random.randint(0, len(allPermutations)-1)
        randomPosition = allPermutations[x]
        return randomPosition

    def getPosition(self):
        return self._position

    def getFitness(self):
        return self._fitness

    def getBestPosition(self):
        return self._bestPosition

    def getBestFitness(self):
        return self._bestFitness

    def setPosition(self, newPosition):
        self._position = newPosition.copy()
        self.evaluate()
        if self._fitness < self._bestFitness:
            self._bestFitness = self._fitness
            self._bestPosition = self._position

    def getSizeOfParticle(self):
        return self._sizeOfParticle

    def __sub__(self, other):
        delta = [abs(a - b) for a, b in zip(self.getPosition(), other.getPosition)]
        return delta
