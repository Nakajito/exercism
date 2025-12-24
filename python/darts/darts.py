from math import sqrt


def score(x, y):
    points = 0

    if sqrt(x**2 + y**2) <= 1:
        points = 10
        return points
    elif sqrt(x**2 + y**2) <= 5:
        points = 5
        return points
    elif sqrt(x**2 + y**2) <= 10:
        points = 1
        return points
    else:
        return points
