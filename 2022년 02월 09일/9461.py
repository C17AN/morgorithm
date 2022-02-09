T = int(input())
dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(5, 101):
    dp.append(dp[-1] + dp[i])

for i in range(T):
    N = int(input())
    print(dp[N - 1])
