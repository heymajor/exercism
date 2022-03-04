import math


def score(x, y):
    calc = math.sqrt(x**2 + y**2)
    if calc <= 1:
        return 10
    elif calc <= 5:
        return 5
    elif calc <= 10:
        return 1
    else:
        return 0
