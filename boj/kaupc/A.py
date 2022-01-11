scoreA, scoreB, scoreC = map(int, input().split())
N = int(input())
group = [[0] * 3 for _ in range(N)]

for i in range(N):
  for j in range(3):
    A, B, C = map(int, input().split())
    scoreSum = A * scoreA + B * scoreB + C * scoreC
    group[i][j] = scoreSum

maxScore = 0
# print(group)
for i in group:
  score = sum(i)
  if maxScore <= score:
    maxScore = score

print(maxScore)