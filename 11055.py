N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    if dp[i] == 0:
        dp[i] = arr[i]
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i]
                # print("dp: ", dp)
print(max(dp))
