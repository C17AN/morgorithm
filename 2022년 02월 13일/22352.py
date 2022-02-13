from collections import deque

N, M = map(int, input().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
cnt = 0
q = deque()

board = [list(map(int, input().split())) for _ in range(N)]
target = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def checkIsSame():
    for row in range(N):
        for col in range(M):
            if board[row][col] - target[row][col] != 0:
                return False
    return True


def BFS(start, value, targetValue):
    y, x = start
    board[y][x] = targetValue
    visited[y][x] = True
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == value and visited[ny][nx] == False:
                    board[ny][nx] = targetValue
                    q.append((ny, nx))
                    visited[ny][nx] = True


for row in range(N):
    for col in range(M):
        if board[row][col] != target[row][col] and visited[row][col] == False:
            BFS((row, col), board[row][col], target[row][col])
            cnt += 1

if cnt <= 1 and checkIsSame():
    print("YES")
else:
    print("NO")
