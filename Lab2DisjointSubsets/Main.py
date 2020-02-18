"""
Disjoint subsets (EA)
___________________________________________________________________________
Consider a set A with n elements and S , S , ..., S subsets of . Partitionate set 1 2 m A
A in two disjoint subsets D and so for all , is not included in either or 1 D2
i = 1, m Si D1
D .
"""
from Algorithm import Algorithm
from Individ import Individ
from Population import Population
from Problem import Problem

"""
>>> s = set([1,2,3])
>>> t = set([1,2])
>>> t.issubset(s)
True
>>> s.issuperset(t)
True
"""


class Application:
    def main(self):
        # s = {1, 2, 3}
        # t = {1, 2}
        # q = {4, 3, 2, 1}
        # w = {4, 3, 2, 1, 6}
        # print(t.issubset(s))
        # print(s.issuperset(t))
        # print(w.issubset(q))

        individ = Individ(6, [1, 2, 3, 4, 5, 6],
                          [{1, 2, 3}, {1, 3}, {4, 5, 6}, {2, 4, 6}, {1, 5, 6}, {1, 3, 5}, {2, 3, 4}, {2, 5, 6}])

        i1 = individ.individual()
        D1, D2 = individ.decodeTheJointSubsets([0, 1, 1, 0, 0, 0])
        print(D1, D2)
        # f = individ.fitness([0, 1, 1, 0, 0, 0])
        # print(f)
        # c1 = individ.crossover([0, 1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1])
        # print(c1)

    def start(self):
        filename = "in.txt"
        probability = 0.01
        populationSize = 50
        noOfIterations = 1000

        problem = Problem(filename)
        A = problem.getA()
        subsets = problem.getSubsets()
        # print(A, subsets)

        individSize = len(A)
        individ = Individ(individSize, A, A, subsets)

        population = Population(populationSize)
        population.computePopulation(A, individSize, subsets)
        algorithm = Algorithm(problem, population)

        graded, fitnessOptim, individualOptim, avgfitness = algorithm.run(noOfIterations, probability, individ)

        print('Result:\n After %d iterations \n Fitness Optim: %d' %
              (noOfIterations, fitnessOptim))
        print(" Individual Optim:" + str(individualOptim))
        meanValue, standardDeviation = algorithm.statistics()
        print("Mean Value: " + str(meanValue))
        print("Standard Deviation: " + str(standardDeviation))
        algorithm.getPlot(avgfitness)


application = Application()
application.start()
