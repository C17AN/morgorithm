N = int(input())
cost = list(map(int, input().split()))
cost.sort()

for i in range(1, N):
    cost[i] = cost[i - 1] + cost[i]

print(sum(cost))
