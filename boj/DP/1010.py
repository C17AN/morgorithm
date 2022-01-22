T = int(input())

table = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    table[1][i] = i

for i in range(1, 10):
    print(i)
for i in range(10, 1, -1):
    print(i)


def dp(N, M):
    if table[N][M]:
        return table[N][M]

    for i in range(M - 1, N - 2, -1):
        table[N][M] += dp(N - 1, i)
    return table[N][M]


for _ in range(T):
    N, M = map(int, input().split())
    print(dp(N, M))
