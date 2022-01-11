N = int(input())

q = []
used = [False] * N

def backtrack(depth):
  if depth == N:
    print(*q)
    return

  for i in range(N):
    if used[i]:
      continue

    q.append(i + 1)
    used[i] = True
    backtrack(depth + 1)
    used[i] = False
    q.pop()

backtrack(0)