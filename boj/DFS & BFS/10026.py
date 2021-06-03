from collections import deque

N = int(input())

board = []
visited = [[False] * N for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

countNormal = 0
countAbNormal = 0

for i in range(N):
    board.append(input())


def normalBFS(node, char):
    global visited
    q = deque()
    q.append(node)
    visited[node[0]][node[1]] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == False and board[ny][nx] == char:
                    q.append((ny, nx))
                    visited[ny][nx] = True


def abnormalBFS(node, char):
    global visited
    q = deque()
    q.append(node)
    visited[node[0]][node[1]] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if char == 'R' or char == 'G':
                    if visited[ny][nx] == False and (board[ny][nx] == 'R' or board[ny][nx] == 'G'):
                        q.append((ny, nx))
                        visited[ny][nx] = True
                if char == 'B':
                    if visited[ny][nx] == False and board[ny][nx] == 'B':
                        q.append((ny, nx))
                        visited[ny][nx] = True


for row in range(N):
    for col in range(N):
        if visited[row][col] == False:
            normalBFS((row, col), board[row][col])
            countNormal += 1

visited = [[False] * N for _ in range(N)]

for row in range(N):
    for col in range(N):
        if visited[row][col] == False:
            abnormalBFS((row, col), board[row][col])
            countAbNormal += 1

print(countNormal, countAbNormal)
