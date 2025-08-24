import copy
from collections import deque
N = int(input())

board = []
height_set = set([])
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

for _ in range(N):
  board.append(list(map(int, input().split())))
  
height_set.add(0.9)
for row in range(N):
  for col in range(N):
    height_set.add(board[row][col])  

height_set = list(height_set)

def BFS(board, visited, start_row, start_col):
  dq = deque([(start_row, start_col)])
  visited[start_row][start_col] = True
  while dq:
    y, x = dq.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0 <= ny < N and 0 <= nx < N:
        if board[ny][nx] != -1 and visited[ny][nx] == False:
          dq.append((ny, nx))
          visited[ny][nx] = True

ans_candidate = []

for i in height_set:
  temp_board = copy.deepcopy(board)
  visited = [[False] * N for _ in range(N)]
  area_count = 0
  for row in range(N):
    for col in range(N):
      if temp_board[row][col] <= i:
        temp_board[row][col] = -1
  
  for row in range(N):
    for col in range(N):
      if temp_board[row][col] != -1 and visited[row][col] == False:
        BFS(temp_board, visited, row, col)
        area_count += 1

  ans_candidate.append(area_count)

print(max(ans_candidate))

# 2
# 1 1
# 1 1
