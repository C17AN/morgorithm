from collections import deque

N, M = map(int, input().split())
board = []

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for y in range(N):
    row = list(map(int, input()))
    board.append(row)

visited = [[False] * M for _ in range(N)]
    
def BFS():
    q = deque([(0, 0)])
    visited[0][0] = True
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == False and board[ny][nx] != 0:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    board[ny][nx] = board[y][x] + 1

BFS()

print(board[N - 1][M - 1])

# 4 6
# 101111
# 101010
# 101011
# 111011