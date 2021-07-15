N = int(input())
arr = list(map(int, input().split()))
dp = [1000] * N

if arr[0] == 1000:
    dp[0] = 0
else:
    dp[0] = 1

count = 0

for i in range(N):
    if dp[i] == 0:
        continue
    for j in range(1, arr[i] + 1):
        # print(i, dp)
        if i + j < N:
            if(dp[i + j] == 1000 or dp[i + j] > dp[i]+1):
                dp[i + j] = min(dp[i+j], dp[i] + 1)


if dp[N - 1] == 1000:
    print(-1)
else:
    print(dp[N-1] - 1)
