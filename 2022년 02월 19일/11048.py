N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

dp[0][0] = arr[0][0]

for row in range(N):
    for col in range(M):
        if 1 <= row < N and 1 <= col < M:
            dp[row][col] = max(dp[row - 1][col] + arr[row][col], dp[row]
                               [col - 1] + arr[row][col], dp[row - 1][col - 1] + arr[row][col], dp[row][col])
        elif 1 <= row < N:
            dp[row][col] = max(dp[row - 1][col] +
                               arr[row][col], dp[row][col])
        elif 1 <= col < M:
            dp[row][col] = max(dp[row][col - 1] +
                               arr[row][col], dp[row][col])

print(dp[N - 1][M - 1])
