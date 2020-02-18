class Problem:
    def __init__(self, filename):
        self.filename = filename
        self.setA, self.subsets = self.readFile()

    def loadData(self):
        file = open(self.filename)
        lines = file.read().split("\n")
        A = []
        for el in lines[0].split(" "):
            A.append(int(el))
        subsets = []
        for i in range(1, len(lines)):
            l2 = []
            l = lines[i].split(" ")
            for el in l:
                l2.append(int(el))
            subsets.append(l2)
        # print(matrix)
        return A, subsets

    # transforms the list of subsets in sets of subsets ;)
    def readFile(self):
        file = open(self.filename)
        lines = file.read().split("\n")
        A = []
        for el in lines[0].split(" "):
            A.append(int(el))
        subsets = []
        for i in range(1, len(lines)):
            l2 = []
            l = lines[i].split(" ")
            for el in l:
                l2.append(int(el))
            subsets.append(set(l2))
        return A, subsets

    def getA(self):
        return self.setA

    def getSubsets(self):
        return self.subsets