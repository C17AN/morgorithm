N, M = map(int, input().split())
visited = [False] * (N + 1)
numberList = []


def backTrack(depth):
    if depth == M:
        print(*numberList)
        return

    for i in range(1, N + 1):
        if visited[i] == False:
            visited[i] = True
            numberList.append(i)
            backTrack(depth + 1)
            visited[i] = False
            numberList.pop()


backTrack(0)