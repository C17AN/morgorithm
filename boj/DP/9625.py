N = int(input())

memo = [1, 1, 2]
memo.extend([0] * 43)


def BABBA(N):
    if N <= 2:
        return memo[N]

    if memo[N] != 0:
        memo[N] = memo[N - 1] + memo[N - 2]
    else:
        memo[N] = BABBA(N - 1) + BABBA(N - 2)

    return memo[N]


print(BABBA(N - 2), BABBA(N - 1))
