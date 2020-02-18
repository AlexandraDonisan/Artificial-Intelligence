import copy
import math
from time import time


class Configuration:
    def __init__(self, positions):
        self.__size = len(positions)
        self.__values = positions[:]
        self.allPossibleValues = [int(i) for i in range(1, self.__size+1)]

    def getSize(self):
        return self.__size

    def getValues(self):
        return self.__values[:]

    def getPossibleValues(self, x, y):
        '''
        :param x: row
        :param y: column
        :return: list with all possible values that the element on position x,y can take
        '''
        existingValues = []
        for i in range(len(self.__values)):
            for j in range(len(self.__values)):
                if self.__values[x][j] in self.allPossibleValues:
                    existingValues.append(self.__values[x][j])
                if self.__values[i][y] in self.allPossibleValues:
                    existingValues.append(self.__values[i][y])
        r = [item for item in self.allPossibleValues if item not in existingValues]

        cubeElements = []
        smallsize = int(math.sqrt(self.__size))
        rowCube = int(x / smallsize)*smallsize
        colCube = int(y / smallsize) * smallsize
        for i in range(rowCube, rowCube+smallsize):
            for j in range(colCube, colCube+smallsize):
                if self.__values[i][j] != 0:
                    cubeElements.append(self.__values[i][j])
        res = [item for item in r if item not in cubeElements]
        return res

    def nextConfig(self, i, j):
        nextC = []

        if self.__values[i][j] == 0:
            #if i < self.__size and j < self.__size:
            #aux = self.__values[:]
            aux = copy.deepcopy(self.getValues())
            convenableValues = self.getPossibleValues(i, j)
            #aux[i][j] = convenableValues[0]
            for el in range(len(convenableValues)):
                aux[i][j] = convenableValues[el] #self in loc sa ramana valoarea initiala se schimba cu cea a lui aux
                nextC.append(Configuration(aux)) #nu face append la nextC, ci inlocuieste valoarea initiala
        return nextC

    def __eq__(self, other):
        if not isinstance(other, Configuration):
            return False
        if self.__size != other.getSize():
            return False
        for i in range(self.__size):
            if self.__values[i] != other.getValues()[i]:
                return False
        return True

    def __str__(self):
        return str(self.__values)


class State:
    '''
    holds a PATH of configurations
    '''

    def __init__(self):
        self.__values = []

    def setValues(self, values):
        self.__values = values[:]

    def getValues(self):
        return self.__values[:]

    def __str__(self):
        s = ''
        for x in self.__values:
            s += str(x) + "\n"
        return s

    def __add__(self, something):
        aux = State()
        if isinstance(something, State):
            aux.setValues(self.__values + something.getValues())
        elif isinstance(something, Configuration):
            aux.setValues(self.__values + [something])
        else:
            aux.setValues(self.__values)
        return aux


class Problem:

    def __init__(self, initial, final):
        self.__initialConfig = initial
        self.__finalConfig = final
        self.__initialState = State()
        self.__initialState.setValues([self.__initialConfig])

    def expand(self, currentState):
        myList = []
        currentConfig = currentState.getValues()[-1]
        for i in range(currentConfig.getSize()):
            for j in range(currentConfig.getSize()):
                for x in currentConfig.nextConfig(i, j):
                    myList.append(currentState + x)

        return myList

    def getFinal(self):
        return self.__finalConfig

    def getRoot(self):
        return self.__initialState

    def heuristics(self, state, finalC):
        l = finalC.getSize()
        count = 2 * l
        for i in range(l):
            if state.getValues()[-1].getValues()[i] != finalC.getValues()[i]:
                count = count - 1
        return count


class Controller:

    def __init__(self, problem):
        self.__problem = problem

    def BFS(self, root):

        q = [root]

        while len(q) > 0:
            currentState = q.pop(0)

            if currentState.getValues()[-1] == self.__problem.getFinal():
                return currentState
            q = q + self.__problem.expand(currentState)

    def BestFS(self, root):

        visited = []
        toVisit = [root]
        while len(toVisit) > 0:
            node = toVisit.pop(0)
            visited = visited + [node]
            if node.getValues()[-1] == self.__problem.getFinal():
                return node
            aux = []
            for x in self.__problem.expand(node):
                if x not in visited:
                    aux.append(x)
            aux = [[x, self.__problem.heuristics(x, self.__problem.getFinal())] for x in aux]
            aux.sort(key=lambda x: x[1])
            aux = [x[0] for x in aux]
            toVisit = aux[:] + toVisit


class UI:

    def __init__(self):
        self.__iniC = Configuration(self.readFile('input1.txt'))
        self.__finC = Configuration(self.readFile('output1.txt'))
        self.__p = Problem(self.__iniC, self.__finC)
        self.__contr = Controller(self.__p)

    def printMainMenu(self):
        self.readFromFile()
        s = '\n'
        s += "0 - exit \n"
        s += "1 - find solution with BFS \n"
        s += "2 - find solution with BestFS\n"
        print(s)

    def findPathBFS(self):
        startClock = time()
        print(str(self.__contr.BFS(self.__p.getRoot())))
        print('execution time = ', time() - startClock, " seconds")

    def findPathBestFS(self):
        startClock = time()
        print(str(self.__contr.BestFS(self.__p.getRoot())))
        print('execution time = ', time() - startClock, " seconds")

    def readFile(self, nameOfFile):
        f = open(nameOfFile, 'r')
        l = [[int(num) for num in line.split(' ')] for line in f]
        return l

    def readFromFile(self):
        f = open('input.txt', 'r')
        n = ""
        l = [[int(num) for num in line.split(' ')] for line in f]
        print("Initial state")
        for i in range(len(l)):
            for j in range(len(l)):
                n += str(l[i][j]) + ' '
            print(n)
            n = ""

    def run(self):
        runM = True
        self.printMainMenu()
        while runM:
            #try:
                command = int(input(">>"))
                if command == 0:
                    runM = False
                elif command == 3:
                    self.readFromFile()
                elif command == 1:
                    self.findPathBFS()
                elif command == 2:

                    self.findPathBestFS()
            #except:
             #   print('invalid command')


def main():
    ui = UI()
    ui.run()
    '''
    l= [[3, 0, 0, 2], [0, 1, 4, 0], [1, 2, 0, 4], [0, 3, 2, 1]]
    existingValues = []
    for i in range(len(l)):
        for j in range(len(l)):
            print(l[0][j])
            if l[0][j] in [1,2,3,4]:
                existingValues.append(l[0][j])
            if l[i][1] in [1,2,3,4]:
                existingValues.append(l[i][1])
    print(existingValues)
    r = [item for item in [1,2,3,4] if item not in existingValues]
    print(r)
    '''

main()
