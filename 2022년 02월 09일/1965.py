N = int(input())
boxList = list(map(int, input().split()))
dp = [0] * N


for i in range(N):
    if dp[i] == 0:
        dp[i] = 1
    for j in range(i):
        if boxList[i] > boxList[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

print(max(dp))
