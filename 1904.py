N = int(input())
dp = [0] * 1000001
dp[0] = 1
dp[1] = 2
dp[2] = 3

for i in range(2, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[N - 1])
