N = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
ans = 0

for i in range(N - 1):
    if price[i] < price[i + 1]:
        price[i + 1] = price[i]

for i in range(N - 1):
    ans += dist[i] * price[i]

print(ans)