from Algorithm import Algorithm
from Problem import Problem


class Controller:
    def __init__(self, filename):
        self._problem = Problem(filename)
        self._algorithm = Algorithm()

    def computeMinCapacities(self):
        capacity = self._problem.getCapacity()
        x = self._problem.getX()
        if len(capacity["small"]) == 3:
            small = self._algorithm.triangular(x, capacity["small"])
        else:
            small = self._algorithm.trapezoidal(x, capacity["small"])

        if len(capacity["medium"]) == 3:
            medium = self._algorithm.triangular(x, capacity["medium"])
        else:
            medium = self._algorithm.trapezoidal(x, capacity["medium"])

        if len(capacity["high"]) == 3:
            high = self._algorithm.triangular(x, capacity["high"])
        else:
            high = self._algorithm.trapezoidal(x, capacity["high"])

        return small, medium, high

    def computeMinTextures(self):
        texture = self._problem.getTexture()
        w = self._problem.getW()
        if len(texture["very soft"]) == 3:
            verySoft = self._algorithm.triangular(w, texture["very soft"])
        else:
            verySoft = self._algorithm.trapezoidal(w, texture["very soft"])

        if len(texture["soft"]) == 3:
            soft = self._algorithm.triangular(w, texture["soft"])
        else:
            soft = self._algorithm.trapezoidal(w, texture["soft"])

        if len(texture["normal"]) == 3:
            normal = self._algorithm.triangular(w, texture["normal"])
        else:
            normal = self._algorithm.trapezoidal(w, texture["normal"])

        if len(texture["resistant"]) == 3:
            resistant = self._algorithm.triangular(w, texture["resistant"])
        else:
            resistant = self._algorithm.trapezoidal(w, texture["resistant"])

        return verySoft, soft, normal, resistant

    def computeCycleTypeMin(self):
        small, medium, high = self.computeMinCapacities()
        verySoft, soft, normal, resistant = self.computeMinTextures()

        delicate = min(small, verySoft)
        easy = max(min(soft, small), min(verySoft, medium), min(normal, small),min(resistant, small))
        normalCycle = max(min(soft, medium), min(normal, medium), min(resistant, medium), min(verySoft, high), min(soft, high))
        intense = max(min(normal, high), min(resistant, high))

        return delicate, easy, normalCycle, intense

    def run(self):
        cycleType = self._problem.getCycle()
        midDelicate = cycleType["delicate"][2]
        midEasy = cycleType["easy"][1]
        midNormal = cycleType["normal"][1]
        midIntense = cycleType["intense"][1]
        # print(midIntense)
        delicate, easy, normalCycle, intense = self.computeCycleTypeMin()
        # print("delicate: " + str(delicate) + "; " + "easy: " + str(easy) + "; "
        #       + "normal cycle: " + str(normalCycle) + "; " + "intense: " + str(intense))
        sumOfMax = delicate + easy + normalCycle + intense
        s = delicate * midDelicate + easy * midEasy + normalCycle * midNormal + intense * midIntense
        v = s / sumOfMax
        return v








