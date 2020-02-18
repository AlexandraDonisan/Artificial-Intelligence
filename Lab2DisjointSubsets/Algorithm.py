import math
import random
import matplotlib.pyplot as plt


class Algorithm:
    def __init__(self, problem, population):
        self.problem = problem
        self.population = population

    def iteration(self, probability):
        pop = self.population.getPopulation()
        i1 = random.randint(0, len(pop) - 1)
        i2 = random.randint(0, len(pop) - 1)
        individ1 = pop[i1]
        individ2 = pop[i2]
        if i1 != i2:
            c = individ1.crossover(individ2)
            c.mutate(probability)
            f1 = individ1.fitness()
            f2 = individ2.fitness()

            fc = c.fitness()
            if f1 > f2 and f1 > fc:
                pop[i1] = c
            if f2 > f1 and f2 > fc:
                pop[i2] = c
        return pop

    def run(self, noOfIterations, probability, individ):
        p = []
        avgfitness = []
        for i in range(noOfIterations):
            p = self.iteration(probability)
            avgfitness.append(self.getAverage(p))

        self.statistics()
        graded = sorted(p)
        result = graded[0]
        fitnessOptim = result.fitness()
        individualOptim = individ.decodeTheJointSubsets(result.A)
        return graded, fitnessOptim, individualOptim, avgfitness

    def getAllFitnesses(self):
        return [individ.fitness() for individ in self.population.getPopulation()]

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
            sum += el.fitness()
        return sum/size
