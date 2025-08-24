from collections import deque

M, N, H = map(int, input().split())

box = []
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
dz = [1, 0, -1]

for level in range(H):
  level_box = []
  for _ in range(N):
    level_box.append(list(map(int, input().split())))
  box.append(level_box)

def BFS(start_z, start_y, start_x):
  visited[start_z][start_y][start_x] = True
  dq = deque([(start_z, start_y, start_x, 0)])
  while dq:
    z, y, x, day = dq.popleft()
    print(z, y, x, day)
    for vertical in range(3):
      for horizontal in range(4):
        nz = z + dz[vertical]
        ny = y + dy[horizontal]
        nx = x + dx[horizontal]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
          if box[nz][ny][nx] == 0 and visited[nz][ny][nx] == False:
            box[nz][ny][nx] = 1
            dq.append((nz, ny, nx, day + 1))
            visited[nz][ny][nx] = True
  return day;

flag = False
answer = -1

for level in range(H):
  for row in range(N):
    for col in range(M):
        if box[level][row][col] == 1 and visited[level][row][col] == False:
          answer = BFS(level, row, col)

for level in range(H):
  for row in range(N):
    for col in range(M):
        if box[level][row][col] == 0:
          flag = True

if flag == True:
  print(-1)
else:
  print(answer)

print(box)


# 3 3 2
# 0 0 0
# 0 0 0
# 0 0 1