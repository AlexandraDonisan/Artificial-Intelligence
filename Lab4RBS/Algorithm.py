import math

class Algorithm:
    def __init__(self):
        pass

    def triangular(self, x, values):
        a = values[0]
        b = values[1]
        c = values[2]
        if b - a == 0:
            first = math.inf
        else:
            first = (x - a) / (b - a)

        if c - b == 0:
            second = math.inf
        else:
            second = (c - x) / (c - b)

        res = max(0, min(first, 1, second))
        return res

    def trapezoidal(self, x, values):
        a = values[0]
        b = values[1]
        c = values[2]
        d = values[3]
        if b - a == 0:
            first = math.inf
        else:
            first = (x - a) / (b - a)

        if d - c == 0:
            second = math.inf
        else:
            second = (d - x) / (d - c)
        res = max(0, min(first, 1, second))
        return res