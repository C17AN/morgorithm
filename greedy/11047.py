N, K = map(int, input().split())
coins = []
sum = 0

for i in range(N):
    coins.append(int(input()))

for j in range(len(coins) - 1, -1, -1):
    sum += K // coins[j]
    K %= coins[j]

print(sum)