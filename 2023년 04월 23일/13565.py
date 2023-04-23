from collections import deque

N, M = map(int, input().split())

board = []
visited = [[False] * M for _ in range(N)]
completed = False

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for _ in range(N):
    board.append(input())


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True

    while q:
        y, x = q.popleft()
        if (y == N - 1):
            return True

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == False and board[ny][nx] == "0":
                    visited[ny][nx] = True
                    q.append((ny, nx))


for i in range(M):
    if (board[0][i] == "0"):
        completed = bfs(0, i)
        if (completed):
            break

if completed:
    print("YES")
else:
    print("NO")
