import operator
from collections import defaultdict
from functools import reduce


class Problem:
    def __init__(self, filename):  # problem data
        self._filename = filename
        self._graph, self._vertices = self.readFromFile()
        self._initialDictionary = self.makeDict()

    def readFromFile(self):
        file = open(self._filename)
        lines = file.read().split("\n")
        Matrix = []
        for i in range(0, len(lines)):
            l2 = []
            l = lines[i].split(" ")
            for el in l:
                l2.append(int(el))
            Matrix.append(l2)
        graph = [x + 1 for x in range(len(Matrix))]
        vertices = []
        for el in Matrix:
            temporary = []
            for i in range(len(el)):
                if el[i] == 1:
                    temporary.append(i + 1)
            vertices.append(temporary)
        return graph, vertices

    def BFS(self, graph, s):  # graph - dictionary
        result = []
        visited = [False] * (len(graph))
        queue = [s]
        visited[s - 1] = True
        while queue:
            s = queue.pop(0)
            result.append(s)
            for i in graph[s]:
                if not visited[i - 1]:
                    queue.append(i)
                    visited[i - 1] = True
        return result

    def makeDict(self):
        G = defaultdict(list)
        for node in range(len(self._graph)):
            G[node + 1].append(self._vertices[node])
        for node in range(len(self._graph)):
            G[node + 1] = reduce(operator.concat, G[node + 1])
        return G

    def getDictionary(self):
        return self._initialDictionary

    def getGraph(self):
        return self._graph

    def getVertices(self):
        return self._vertices
