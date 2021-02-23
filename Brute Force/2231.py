N = int(input())


def getEachValue(n):
    value = 0
    while n != 0:
        value += (n % 10)
        n = int(n / 10)
    return value


def getPartialSum():
    for i in range(N):
        if i + getEachValue(i) == N:
            return i
    return 0


print(getPartialSum())
