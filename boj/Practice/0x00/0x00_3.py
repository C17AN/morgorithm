import math


def func3(n):
    if math.sqrt(n) % 1 == 0:
        return 1
    return 0


print(func3(693953651))