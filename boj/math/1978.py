N = int(input())
numbers = list(map(int, input().split()))
table = [i for i in range(1, 1001)]
cnt = 0


def eratos(N):
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            if j % i == 0:
                table[j] = 0


eratos(100)
print(table)
