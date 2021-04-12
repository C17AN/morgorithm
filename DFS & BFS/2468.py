from collections import deque

N = int(input())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
area = []
visited = [[False] * N for _ in range(N)]
height = 0
safe_cnt = 0
max_safe_cnt = 0

for i in range(N):
    area.append(list(map(int, input().split())))

height = max(max(area))


def bfs_make_sink(start_node, height):
    y, x = start_node
    q = deque()
    visited[y][x] = True
    q.append(start_node)
    while q:
        y, x = q.popleft()

        if area[y][x] > height:
            safe[y][x] = True

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == False:
                    visited[ny][nx] = True
                    q.append((ny, nx))


def bfs_get_safe(start_node):
    y, x = start_node
    q = deque()
    q.append(start_node)
    visited[y][x] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == False and safe[ny][nx] == True:
                    visited[ny][nx] = True
                    q.append((ny, nx))


for i in range(0, height + 1):
    safe_cnt = 0
    safe = [[False] * N for _ in range(N)]
    bfs_make_sink((0, 0), i)
    visited = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if visited[row][col] == False and safe[row][col] == True:
                bfs_get_safe((row, col))
                safe_cnt += 1

    if safe_cnt >= max_safe_cnt:
        max_safe_cnt = safe_cnt

    visited = [[False] * N for _ in range(N)]
    # print('#height: {}'.format(i))
    # print(safe)

print(max_safe_cnt)