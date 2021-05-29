from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomatoes = []
dy = [1, 0, -1, 0, N, -N]
dx = [0, 1, 0, -1, 0, 0]
fresh = deque()

for h in range(H):
    for i in range(N):
        tomatoes.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N * H)]


def BFS(freshList):
    while freshList:
        y, x = freshList.popleft()
        visited[y][x] = True
        for h in range(H - 1):
            for i in range(6):
                ny = y + dy[i]
                nx = x + dx[i]
                print(y, x, '/', ny, nx)
                print(tomatoes)
                # print(visited)
                # print(freshList)
                if h * N <= ny < h * N + N and 0 <= nx < M:
                    if visited[ny][nx] == False and tomatoes[ny][
                            nx] == 0 and tomatoes[ny][nx] != -1:
                        freshList.append((ny, nx))
                        tomatoes[ny][nx] = tomatoes[y][x] + 1
                        visited[ny][nx] = True


def check_tomatoes():
    max_day = 0
    for row in range(N):
        for col in range(M):
            if tomatoes[row][col] == 0:
                return -1
            elif tomatoes[row][col] >= max_day:
                max_day = tomatoes[row][col]

    return max_day - 1


# 층은 0층부터 시작
for row in range(N * H):
    for col in range(M):
        if tomatoes[row][col] == 1:
            fresh.append((row, col))

BFS(fresh)

print(check_tomatoes())