import random

from Individ import Individ


class Population:
    def __init__(self, noOfIndivids):
        self.noOfIndivids = noOfIndivids
        self.individs = []

    def computePopulation(self, initialList, individSize, subsets):
        for i in range(self.noOfIndivids):
            x = [random.randint(0, 1) for x in range(individSize)]
            self.individs.append(Individ(individSize, initialList, x, subsets))

    def evaluate(self):
        pass

    def selection(self):
        pass

    def getPopulation(self):
        return self.individs

    def __str__(self):
        res =[]
        for el in self.individs:
            res.append(el)
        return str(res)