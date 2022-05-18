N = int(input())

arr = [(0, 0)] * (N + 1)
dp = [0] * (2000)

for day in range(1, N + 1):
    T, P = map(int, input().split())
    arr[day] = (T, P)

for day in range(1, N + 1):
    T, P = arr[day]
    dp[day + T - 1] = max(dp[day + T - 1], max(dp[0:day]) + P)

print(max(dp[1:N + 1]))
