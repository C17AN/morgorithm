from collections import deque
N = int(input())

board = []
maxScore = 0
diag_dy = [1, 1, -1, -1]
diag_dx = [-1, 1, 1, -1]

for i in range(N):
  board.append(list(map(int, input().split())))


def DIAG_BFS(startNode):
  score = 1
  y, x = startNode
  q = deque()
  q.append(startNode)
  visited[y][x] = True
  while q:
    y, x = q.popleft()
    for i in range(4):
      ny = y + diag_dy[i]
      nx = x + diag_dx[i]
      if 0 <= ny < N and 0 <= nx < N:
        if visited[ny][nx] == False:
          q.append((ny, nx))
          visited[ny][nx] = True
          if board[ny][nx] == 1:
            score += 1
  return score

def getYSum(col):
  score = 0
  for row in range(N):
    if board[row][col] != 2:
      score += board[row][col]
  return score

for row in range(N):
  for col in range(N):
    if board[row][col] == 2:
      visited = [[False] * N for _ in range(N)]
      board[row][col] = 1
      x_score = sum(board[row])
      y_score = getYSum(col)
      diag_score = DIAG_BFS((row, col))
      score = max(x_score, y_score, diag_score)
      print(x_score, y_score, diag_score)
      if score >= maxScore:
        maxScore = score
      board[row][col] = 2
  
print(maxScore)