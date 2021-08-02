import sys
input = sys.stdin.readline
N, M = map(int, input().split())

numberList = list(map(int, input().split()))
numberList.sort()

result = [0] * M


def backtrack(start, depth):
    global used
    latest = 0
    if depth == M:
        for i in range(M):
            print(result[i], end=" ")
        print()
        return

    for i in range(start, N):
        if numberList[i] != latest:
            result[depth] = numberList[i]
            latest = result[depth]
            backtrack(i, depth + 1)


backtrack(0, 0)
