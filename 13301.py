N = int(input())

arr = [0] * 81
dp = [0] * 81
dp[0] = 4
dp[1] = 6
dp[2] = 10


def fib(N):
    if N == 2:
        return dp[2]
    if dp[N - 1]:
        dp[N] = dp[N - 1] + dp[N - 2]
    else:
        dp[N] = fib(N - 1) + fib(N - 2)
    return dp[N]


fib(80)
print(dp[N - 1])
