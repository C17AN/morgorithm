N, M = map(int, input().split())

numberList = list(map(int, input().split()))
numberList.sort()
result = []


def backtrack(depth, start):
    if depth == M:
        print(*result)
        return
    for i in range(start, N):
        result.append(numberList[i])
        backtrack(depth + 1, i)
        result.pop()


backtrack(0, 0)
