import sys
input = sys.stdin.readline
N, M = map(int, input().split())

numberList = list(map(int, input().split()))
numberList.sort()

result = [0] * M
used = [False] * N


def backtrack(depth):
    global used
    latest = 0
    if depth == M:
        for i in range(M):
            print(result[i], end=" ")
        print()
        return

    for i in range(N):
        if used[i] is False and numberList[i] != latest:
            result[depth] = numberList[i]
            latest = result[depth]
            used[i] = True
            backtrack(depth + 1)
            used[i] = False


backtrack(0)
