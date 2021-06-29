import math
H, Y = map(int, input().split())

dp = [1] * 11
dp[0] = H

for i in range(1, 11):
    dp[i] = math.floor(dp[i - 1] * 1.05)
    if i >= 3:
        dp[i] = math.floor(max(dp[i - 1] * 1.05, dp[i - 3] * 1.2))
    if i >= 5:
        dp[i] = math.floor(
            max(dp[i - 1] * 1.05, dp[i - 3] * 1.2, dp[i - 5] * 1.35))

print(dp[Y])
