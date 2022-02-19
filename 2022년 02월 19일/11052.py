N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

# 카드 N개를 샀을 때 가능한 최대 가격 (이 때, N번째 카드는 N개의 개수를 차지한다고 생각한다.)
dp = [0] * (N + 1)
# dp[1] = arr[1] * N


for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i - j] + arr[j], dp[i])
        # print(i, j, dp[1:])

print(max(dp))
