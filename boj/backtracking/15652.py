N, M = map(int, input().split())

visited = []
numberList = []


def backTrack(depth, start):
    if depth == M:
        print(*numberList)
        return
    for i in range(start, N + 1):
        numberList.append(i)
        backTrack(depth + 1, i)
        numberList.pop()


backTrack(0, 1)
