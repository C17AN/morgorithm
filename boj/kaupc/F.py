from collections import deque
N = int(input())

board = []
maxScore = 0
# dy = [1, 1, 0, -1, -1, -1, 0, 1]
# dx = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(N):
  board.append(list(map(int, input().split())))

def maxScoreChecker(N):
  maxScore = 0
  score = 0

  # 행의 합
  for row in range(N):
      score = sum(board[row])
      if maxScore <= score:
        maxScore = score
  
  # 열의 합
  colBoard = zip(*board)
  tempScore = 0
  for column in colBoard:
    tempScore = sum(column)
    if maxScore <= tempScore:
      maxScore = tempScore  
  
  # 대각선의 합
  for diag in range(N):
    ""
  return maxScore

# def BFS(startNode):
#   score = 0
#   y, x = startNode
#   q = deque()
#   q.append(startNode)
#   visited[y][x] = True
#   while q:
#     y, x = q.popleft()
#     for i in range(8):
#       ny = y + dy[i]
#       nx = x + dx[i]
#       if 0 <= ny < N and 0 <= nx < N:
#         if visited[ny][nx] == False and board[ny][nx] == 1:
#           q.append((ny, nx))
#           visited[ny][nx] = True

for row in range(N):
  for col in range(N):
    if board[row][col] == 2:
      # visited = [[False] * N for _ in range(N)]
      board[row][col] = 1
      # BFS((row, col))
      score = maxScoreChecker(N)
      if score >= maxScore:
        maxScore = score
      board[row][col] = 2
  
print(maxScore)