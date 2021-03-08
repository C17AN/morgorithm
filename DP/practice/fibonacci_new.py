N = int(input())
memo = [0] * 10000001


def fib(N):
    if N == 1 or N == 0:
        memo[N] = N
        return memo[N]
    if memo[N] != 0:
        return memo[N]
    else:
        memo[N] = (fib(N - 1) + fib(N - 2)) % 1000000007
        return memo[N]


print(fib(N))