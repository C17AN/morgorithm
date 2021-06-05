N, M = map(int, input().split())

visited = []
numberList = []


def backTrack(depth, start):
    if depth == M:
        print(*numberList)
        return

    for i in range(start, N + 1):
        if i not in visited:
            numberList.append(i)
            visited.append(i)
            backTrack(depth + 1, i + 1)
            numberList.pop()
            visited.pop()


backTrack(0, 1)
