from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
board = [list(input()) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

whiteScore, blueScore = 0, 0


def WhiteBFS(startNode):
    y, x = startNode
    whiteCount = 1
    visited[y][x] = True
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < M and 0 <= nx < N:
                if visited[ny][nx] == False and board[ny][nx] == "W":
                    whiteCount += 1
                    visited[ny][nx] = True
                    q.append((ny, nx))

    return whiteCount**2


def BlueBFS(startNode):
    y, x = startNode
    blueCount = 1
    visited[y][x] = True
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < M and 0 <= nx < N:
                if visited[ny][nx] == False and board[ny][nx] == "B":
                    blueCount += 1
                    visited[ny][nx] = True
                    q.append((ny, nx))

    return blueCount**2


for row in range(M):
    for col in range(N):
        if visited[row][col] == False:
            if board[row][col] == "W":
                whiteScore += WhiteBFS((row, col))
            elif board[row][col] == "B":
                blueScore += BlueBFS((row, col))

print(whiteScore, blueScore)
