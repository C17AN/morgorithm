from collections import deque

T = int(input())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def BFS(startNode):
  y, x = startNode
  q = deque()
  visited[y][x] = True
  q.append((y, x))

  while q:
    y, x = q.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0 <= ny < H and 0 <= nx < W:
        if board[ny][nx] == '#' and visited[ny][nx] == False:
          q.append((ny, nx))
          visited[ny][nx] = True


for i in range(T):
  cnt = 0
  H, W = map(int, input().split())
  board = []
  for i in range(H):
    temp = input()
    board.append([])
    for j in range(W):
      board[i].append(temp[j])
  visited = [[False] * W for _ in range(H)]
  for row in range(H):
    for col in range(W):
        if visited[row][col] == False and board[row][col] == '#':
            BFS((row, col))
            cnt += 1
  print(cnt)


