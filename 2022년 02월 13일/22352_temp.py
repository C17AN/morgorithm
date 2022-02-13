from collections import deque

N, M = map(int, input().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
cnt = 0
q = deque()

board = [list(map(int, input().split())) for _ in range(N)]
target = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        board[i][j] -= target[i][j]


def BFS(start, value):
    y, x = start
    visited[y][x] = True
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == value and visited[ny][nx] == False:
                    board[ny][nx] = 0
                    q.append((ny, nx))
                    visited[ny][nx] = True


print(board)


for row in range(N):
    for col in range(M):
        if board[row][col] != 0 and visited[row][col] == False:
            BFS((row, col), board[row][col])
            cnt += 1

print(board)

if cnt <= 1:
    print("YES")
else:
    print("NO")
