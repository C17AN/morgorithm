N = int(input())

d = [-1] * 100001
d[2] = 1
d[4] = 2
d[5] = 1

for i in range(5, N + 1):
    if d[i - 2] == -1 and d[i - 5] == -1:
        continue
    if d[i - 2] == -1:
        d[i] = 1 + d[i - 5]
    elif d[i - 5] == -1:
        d[i] = 1 + d[i - 2]
    else:
        d[i] = 1 + min(d[i - 2], d[i - 5])

print(d[N])
