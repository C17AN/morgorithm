from collections import deque

N, M, K = map(int, input().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

board = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

max_size = 0


def BFS(node):
    global board
    global visited
    q = deque()
    q.append(node)
    visited[node[0]][node[1]] = True
    size = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == False and board[ny][nx] != 0:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    board[ny][nx] = 0
                    size += 1

    return size


for _ in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1

for row in range(N):
    for col in range(M):
        if board[row][col] != 0 and visited[row][col] == False:
            max_size = max(max_size, BFS((row, col)))

print(max_size)