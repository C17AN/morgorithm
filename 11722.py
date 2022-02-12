N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
cnt = 0

for i in range(len(arr)):
    if dp[i] == 0:
        dp[i] = 1

    for j in range(i):
        if arr[i] < arr[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

print(max(dp))
