from collections import deque
N, M = map(int, input().split())
max_cnt = 0
queue = deque()
board = []

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(N):
    board.append(list(map(int, input().split())))


def BFS(q):
    while q:
        y, x = q.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == 0:
                    board[ny][nx] = board[y][x] + 1
                    q.append((ny, nx))


for row in range(N):
    for col in range(M):
        if board[row][col] == 1:
            queue.append((row, col))

BFS(queue)

for row in range(N):
    for col in range(M):
        if board[row][col] >= max_cnt:
            max_cnt = board[row][col]

print(max_cnt - 1)
