import math
import copy
from time import time


class Problem:
    def __init__(self, filename):
        self.__filename = filename
        self.__board = self.readFromFile()
        self.allPossibleValues = [int(i) for i in range(1, self.getSize() + 1)]

    def readFromFile(self):
        f = open(self.__filename, 'r')
        initialConfig = [[int(num) for num in line.split(' ')] for line in f]
        # print(initialConfig)
        return initialConfig

    def getSize(self):
        return len(self.__board)

    def getBoard(self):
        return self.__board

    def showBoard(self):
        board = ""
        for i in range(self.getSize()):
            for j in range(self.getSize()):
                board += str(self.__board[i][j]) + ' '
            print(board)
            board = ""

    def getFirstEmpty(self, board):
        for row in range(self.getSize()):
            for col in range(self.getSize()):
                if board[row][col] == 0:
                    return row, col
        return -1, -1

    def getPossibleValues(self, x, y, board):
        '''
        :param x: row
        :param y: column
        :return: list with all possible values that the element on position x,y can take
        '''
        existingValues = []
        for i in range(self.getSize()):
            for j in range(self.getSize()):
                if board[x][j] in self.allPossibleValues:
                    existingValues.append(board[x][j])
                if board[i][y] in self.allPossibleValues:
                    existingValues.append(board[i][y])
        rowColElems = [item for item in self.allPossibleValues if item not in existingValues]

        cubeElements = []
        lenOfCube = int(math.sqrt(self.getSize()))
        rowCube = int(x / lenOfCube) * lenOfCube
        colCube = int(y / lenOfCube) * lenOfCube
        for i in range(rowCube, rowCube + lenOfCube):
            for j in range(colCube, colCube + lenOfCube):
                if board[i][j] != 0:
                    cubeElements.append(board[i][j])
        possibleValues = [item for item in rowColElems if item not in cubeElements]
        return possibleValues

    def isSolved(self, boardState):
        finalSum = sum(range(1, self.getSize() + 1))

        # checks if the sum of the rows and columns are equal to the
        # sum of all numbers from 1 to n(n = size of the board)
        for row in range(self.getSize()):
            if sum(boardState[row]) != finalSum:
                return False
            columnSum = 0
            for col in range(self.getSize()):
                columnSum += boardState[row][col]

            if columnSum != finalSum:
                return False

        # checks if the sum of all numbers from one small cube
        # is equal to the sum of all numbers from 1 to n(n = size of the board)
        cubeWidth = math.ceil(math.sqrt(self.getSize()))
        cubeHeight = int(self.getSize() / math.ceil(math.sqrt(self.getSize())))
        for col in range(0, self.getSize(), cubeWidth):
            for row in range(0, self.getSize(), cubeHeight):
                cubeSum = 0
                for cubeRow in range(0, cubeHeight):
                    for cubeCol in range(0, cubeWidth):
                        cubeSum += boardState[row + cubeRow][col + cubeCol]
                if cubeSum != finalSum:
                    return False

        return True

    # returns updated board after adding a new value
    def updateBoardState(self, boardState, action):
        newState = copy.deepcopy(boardState)
        value = action[0]
        row = action[1]
        column = action[2]
        newState[row][column] = value
        return newState

    def expand(self, boardState):
        row, col = self.getFirstEmpty(boardState)
        action = []
        result = []
        possibleValues = self.getPossibleValues(row, col, boardState)
        for el in possibleValues:
            action.append(el)
            action.append(row)
            action.append(col)
            result.append(self.updateBoardState(boardState, action))
            action = []
        return result

    def heuristics(self, state1, state2):
        row1, col1 = self.getFirstEmpty(state1)
        row2, col2 = self.getFirstEmpty(state2)

        allVal1 = self.getPossibleValues(row1, col1, state1)
        allVal2 = self.getPossibleValues(row2, col2, state2)
        if len(allVal1) < len(allVal2):
            return True
        return False


class Controller:
    def __init__(self, problem):
        self.__problem = problem

    def getProblem(self):
        return self.__problem

    def BFS(self, root):
        if self.__problem.isSolved(root):
            return self.__problem.getBoard()
        q = [root]
        while len(q) > 0:
            currentState = q.pop(0)
            if self.__problem.isSolved(currentState):
                return currentState
            q = q + self.__problem.expand(currentState)

    def BestFS(self, root):

        visited = []
        toVisit = [root]
        while len(toVisit) > 0:
            node = toVisit.pop(0)
            visited = visited + [node]
            if self.__problem.isSolved(node):
                return node
            aux = []
            for x in self.__problem.expand(node):
                if x not in visited:
                    aux.append(x)
            aux = self.orderStates(aux)
            # aux = [[x, self.__problem.heuristics(x, self.__problem.getFinal())] for x in aux]
            # aux.sort(key=lambda x: x[1])
            # aux = [x[0] for x in aux]

            toVisit = aux[:] + toVisit

    def orderStates(self, state):
        n = len(state)
        for i in range(n):
            for j in range(0, n - i - 1):
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if self.__problem.heuristics(state[j], state[j+1]):
                    state[j], state[j + 1] = state[j + 1], state[j]
        return state


class UI:
    def __init__(self, ctrl):
        self.__ctrl = ctrl

    def printMainMenu(self):
        self.__ctrl.getProblem().showBoard()
        s = '\n'
        s += "0 - exit \n"
        s += "1 - find solution with BFS \n"
        s += "2 - find solution with BestFS\n"
        print(s)

    @staticmethod
    def printBoard(board):
        boardP = ""
        for i in range(len(board)):
            for j in range(len(board)):
                boardP += str(board[i][j]) + ' '
            print(boardP)
            boardP = ""

    def findPathBFS(self):
        startClock = time()
        root = self.__ctrl.getProblem().getBoard()
        res = self.__ctrl.BFS(root)
        self.printBoard(res)
        print('execution time = ', time() - startClock, " seconds")

    def findPathBestFS(self):
        startClock = time()
        root = self.__ctrl.getProblem().getBoard()
        res = self.__ctrl.BestFS(root)
        self.printBoard(res)
        print('execution time = ', time() - startClock, " seconds")

    def run(self):
        runM = True
        self.printMainMenu()
        while runM:
            command = int(input(">>"))
            if command == 0:
                runM = False
            elif command == 1:
                self.findPathBFS()
            elif command == 2:
                self.findPathBestFS()


def main():
    problem = Problem("init2.txt")
    problem.isSolved(problem.getBoard())
    ctrl = Controller(problem)
    ui = UI(ctrl)
    ui.run()


main()
