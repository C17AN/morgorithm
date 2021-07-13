N, P, Q = map(int, input().split())
usedMap = {0: 1}


def getSeq(N):
    try:
        if usedMap[N]:
            return usedMap[N]
    except:
        usedMap[N] = getSeq(N // P) + getSeq(N // Q)
        return usedMap[N]


print(getSeq(N))
