import random


class Individ:
    def __init__(self, size, initialList, A, sublists):
        self.size = size  # size of an individual
        self.initialList = initialList
        self.A = A
        self.sublists = sublists  # the given sublists

    def individual(self):
        return [random.randint(0, 1) for x in range(self.size)]
        # newSet = [random.randint(0, 1) for x in range(self.size)]
        # return Individ(self.size, newSet, self.sublists)

    def decodeTheJointSubsets(self, individual):
        D1 = []
        D2 = []
        for i in range(len(individual)):
            if individual[i] == 0:
                D1.append(self.initialList[i])
            else:
                D2.append(self.initialList[i])
        return D1, D2

    def fitness(self):
        """
        If the fitness is 0 then the individual is a solution, otherwise it is not
        :param individual: the set A of numbers
        :return: the fitness
        """
        individual = self.A
        f = 0  # fitness is equal to 0 at first
        D1, D2 = self.decodeTheJointSubsets(individual)
        sD1 = set(D1)
        sD2 = set(D2)
        for el in self.sublists:
            if el.issubset(sD1) or el.issubset(sD2):
                f += 1
        return f

    def mutate(self, probability):
        individual = self
        if probability > random.random():
            index = random.randint(0, len(individual.A) - 1)
            if individual.A[index] == 1:
                individual.A[index] = 0
            else:
                individual.A[index] = 1
        #return individual.A

    def crossover(self, individ1):
        child1 = []
        child2 = []
        individ2 = self

        middle = int(len(individ1.A) / 2)
        for i in range(len(individ1.A)):
            if i < middle:
                child1.append(individ1.A[i])
                child2.append(individ2.A[i])
            else:
                child1.append(individ2.A[i])
                child2.append(individ1.A[i])
        # return [child1, child2]
        return Individ(self.size, self.initialList, child1, self.sublists)

    def __lt__(self, other):
        return self.fitness() < other.fitness()


