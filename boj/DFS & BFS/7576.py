from collections import deque

M, N = map(int, input().split())
tomatoes = []
visited = [[False] * M for _ in range(N)]
start_nodes = []
cnt = 0

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for i in range(N):
    tomatoes.append(list(map(int, input().split())))


def BFS(start_node_list):
    q = deque()
    for i in start_node_list:
        q.append(i)
    while q:
        y, x = q.popleft()
        visited[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == False and tomatoes[ny][
                        nx] != -1 and tomatoes[ny][nx] == 0:
                    q.append((ny, nx))
                    tomatoes[ny][nx] = tomatoes[y][x] + 1
                    visited[ny][nx] = True


def check_tomatoes():
    max_day = 0
    for row in range(N):
        for col in range(M):
            if tomatoes[row][col] == 0:
                return -1
            else:
                if tomatoes[row][col] - 1 > max_day:
                    max_day = tomatoes[row][col] - 1
    return max_day


for row in range(N):
    for col in range(M):
        if tomatoes[row][col] == 1 and visited[row][col] == False:
            start_nodes.append((row, col))
BFS(start_nodes)

print(check_tomatoes())