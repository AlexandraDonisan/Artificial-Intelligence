from capacity import *
from texture import *
from cycle import *


class Problem:
    def __init__(self, filename):
        self._filename = filename
        self._texture = self.loadTextureFromFile()
        self._capacity = self.loadCapacityFromFile()
        self._cycle = self.loadCycleTypeFromFile()
        self._x, self._w = self.loadParametersFromFile()


    def loadTextureFromFile(self):
        texture = {
            "very soft": list(VERY_SOFT),
            "soft": list(SOFT),
            "normal": list(NORMAL),
            "resistant": list(RESISTANT)
        }
        print(texture)
        return texture

    def loadCapacityFromFile(self):
        capacity = {
            "small": list(SMALL),
            "medium": list(MEDIUM),
            "high": list(HIGH)
        }
        print(capacity)
        return capacity

    def loadCycleTypeFromFile(self):
        cycleType = {
            "delicate": list(DELICATE),
            "easy": list(EASY),
            "normal": list(NORMAL),
            "intense": list(INTENSE)
        }
        print(cycleType)
        return cycleType

    def loadParametersFromFile(self):
        file = open(self._filename)
        params = file.read().split(" ")
        x = float(params[0])
        w = float(params[1])
        return x, w

    def getTexture(self):
        return self._texture

    def getCapacity(self):
        return self._capacity

    def getCycle(self):
        return self._cycle

    def getX(self):
        return self._x

    def getW(self):
        return self._w













    # def textureEx(self):
    #     small = []
    #     medium = []
    #     high = []
    #     for el in SMALL:
    #         small.append(el)
    #     print(small)
    #
    #     for el in MEDIUM:
    #         medium.append(el)
    #     print(medium)
    #
    #     for el in HIGH:
    #         high.append(el)
    #     print(high)
    #
    # def capacityEx(self):
    #     verySoft = []
    #     soft = []
    #     normal = []
    #     resistant = []
    #
    #     for el in VERY_SOFT:
    #         verySoft.append(el)
    #     for el in SOFT:
    #         soft.append(el)
    #     for el in NORMAL:
    #         normal.append(el)
    #     for el in RESISTANT:
    #         resistant.append(el)
    #     print(verySoft, soft, normal, resistant)
