N = int(input())
memo = [0] * 91


def pin(n):
    if n == 0:
        memo[n] = 0
        return memo[n]
    elif n == 1:
        memo[n] = 1
        return memo[n]
    else:
        if memo[n] == 0:
            memo[n] = pin(n - 1) + pin(n - 2)
            return memo[n]
        else:
            return memo[n]


print(pin(N))