N = int(input())

d = [[0, 0, 0] for i in range(1000)]

for i in range(N):
    d[i] = list(map(int, input().split()))


for i in range(1, N):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + d[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + d[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + d[i][2]

print(min(d[N - 1]))
