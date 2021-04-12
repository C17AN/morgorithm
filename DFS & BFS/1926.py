from collections import deque

N, M = map(int, input().split())
picture = []
# visited = [[False] * M] * N
visited = [[False] * M for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
picture_cnt = 0
max_picture = 0

for _ in range(N):
    picture.append(list(map(int, input().split())))


def BFS(start_node):
    cnt = 0
    q = deque()
    y, x = start_node
    q.append((y, x))
    visited[y][x] = True

    while q:
        y, x = q.pop()
        cnt += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == False and picture[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx))

    return cnt


for row in range(N):
    for col in range(M):
        if picture[row][col] == 1 and visited[row][col] == False:
            cnt = BFS((row, col))
            picture_cnt += 1
            if cnt > max_picture:
                max_picture = cnt

print(picture_cnt)
print(max_picture)