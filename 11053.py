N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N


for i in range(N):
    if not dp[i]:
        dp[i] = 1
    for j in range(i):
        if arr[i] > arr[j]:
            # print("dp", dp)
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

print(max(dp))
