N, M = map(int, input().split())

numberList = list(map(int, input().split()))
numberList.sort()
visited = []


def backtracking(depth):
    if depth == M:
        print(*visited)
        return

    for i in range(0, N):
        visited.append(numberList[i])
        backtracking(depth + 1)
        visited.pop()


backtracking(0)
