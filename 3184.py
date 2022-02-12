from collections import deque

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

survivedWolves = 0
survivedSheeps = 0

q = deque()


def BFS(start):
    y, x = start
    visited[y][x] = True
    q.append((y, x))
    sheeps = 0
    wolves = 0

    while q:
        y, x = q.popleft()
        if board[y][x] == 'o':
            sheeps += 1
        elif board[y][x] == 'v':
            wolves += 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if visited[ny][nx] == False and board[ny][nx] != '#':
                    q.append((ny, nx))
                    visited[ny][nx] = True

    return sheeps, wolves


for row in range(R):
    for col in range(C):
        if board[row][col] != '#' and visited[row][col] == False:
            sheeps, wolves = BFS((row, col))
            if sheeps > wolves:
                survivedSheeps += sheeps
            else:
                survivedWolves += wolves


print(survivedSheeps, survivedWolves)
