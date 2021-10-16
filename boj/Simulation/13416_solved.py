T = int(input())
for i in range(T):
  totalReturn = 0
  N = int(input())
  for _ in range(N):
    maxReturn = max(map(int, input().split()))
    if maxReturn < 0:
      continue
    totalReturn += maxReturn
  print(totalReturn)
