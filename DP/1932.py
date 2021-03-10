N = int(input())

t = [0]

for i in range(N):
    t.append(list(map(int, input().split())))

for i in reversed(range(N)):
    for j in range(i):
        t[i][j] = t[i][j] + max(t[i + 1][j], t[i + 1][j + 1])

print(*t[1])