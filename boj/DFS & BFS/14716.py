from collections import deque
N, M = map(int, input().split())

visited = [[False] * M for _ in range(N)]
board = []
count = 0

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def BFS(node):
    q = deque()
    q.append(node)
    visited[node[0]][node[1]]
    while q:
        y, x = q.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == False and board[ny][nx] == 1:
                    q.append((ny, nx))
                    visited[ny][nx] = True


for row in range(N):
    board.append(list(map(int, input().split())))

for row in range(N):
    for col in range(M):
        if board[row][col] == 1 and visited[row][col] == False:
            BFS((row, col))
            count += 1

print(count)
