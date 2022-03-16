from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def MELT_BFS(startNode):
    y, x = startNode
    q = deque()
    q.append((y, x))
    meltVisited[y][x] = True
    while q:
        y, x = q.popleft()
        seaCount = 0

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if copiedBoard[ny][nx] == 0:
                seaCount += 1

        board[y][x] -= seaCount
        if board[y][x] < 0:
            board[y][x] = 0

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if copiedBoard[ny][nx] != 0 and meltVisited[ny][nx] == False:
                    q.append((ny, nx))
                    meltVisited[ny][nx] = True


def CHECK_BFS(startNode):
    y, x = startNode
    q = deque()
    q.append((y, x))
    checkVisited[y][x] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] != 0 and checkVisited[ny][nx] == False:
                    q.append((ny, nx))
                    checkVisited[ny][nx] = True
    return 1


year = 0

while 1:
    islandCount = 0
    meltVisited = [[False] * M for _ in range(N)]
    checkVisited = [[False] * M for _ in range(N)]
    copiedBoard = deepcopy(board)

    for row in range(N):
        for col in range(M):
            if board[row][col] != 0 and meltVisited[row][col] == False:
                MELT_BFS((row, col))

    for row in range(N):
        for col in range(M):
            if board[row][col] != 0 and checkVisited[row][col] == False:
                islandCount += CHECK_BFS((row, col))
    year += 1
    if islandCount > 1:
        print(year)
        break

    elif islandCount == 0:
        print(0)
        break
