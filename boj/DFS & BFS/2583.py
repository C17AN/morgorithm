from collections import deque

M, N, K = map(int, input().split())
board = [[0] * N for i in range(M)]
visited = [[False] * N for i in range(M)]
size_list = []
cnt = 0

for i in range(K):
    dx, dy, ux, uy = map(int, input().split())
    for row in range(dy, uy):
        for col in range(dx, ux):
            board[row][col] = 1

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def BFS(start_node):
    global cnt
    cnt += 1
    size = 1
    q = deque()
    q.append(start_node)
    while q:
        y, x = q.popleft()
        visited[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < M and 0 <= nx < N:
                if visited[ny][nx] == False and board[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    size += 1

    size_list.append(size)


for row in range(M):
    for col in range(N):
        if board[row][col] == 0 and visited[row][col] == False:
            BFS((row, col))

size_list.sort()

print(cnt)
print(*size_list)