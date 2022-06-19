N = int(input())

d = [9999] * (N + 1)

for i in range(1, N + 1):
    if i % 3 == 0 and i % 5 == 0:
        d[i] = min(i // 3, i // 5)
    elif i % 3 == 0:
        d[i] = min(d[i - 3] + 1, i // 3)
    elif i % 5 == 0:
        d[i] = min(d[i - 5] + 1, i // 5)
    else:
        d[i] = min(d[i - 3] + 1, d[i - 5] + 1)

if d[N] > 9999:
    print(-1)
else:
    print(d[N])
