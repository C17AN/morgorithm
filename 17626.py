N = int(input())
d = [0] * (N + 1)
d[1] = 1

for i in range(1, N + 1):
    d[i] = d[1] + d[i - 1]
    for j in range(i + 1):
        if j**2 > i:
            break
        d[i] = min(1 + d[i - j * j], d[i])


print(d[N])
