T = int(input())

memo_zero = [0, 1] + [0] * 39
memo_one = [0, 1] + [0] * 39


def fib_zero(n):
    if n == 0:
        return 1
    elif n == 1:
        memo_zero[1] = 0
        return memo_zero[1]
    else:
        if memo_zero[n] == 0:
            memo_zero[n] = fib_zero(n - 2) + fib_zero(n - 1)
            return memo_zero[n]
        else:
            return memo_zero[n]


def fib_one(n):
    if n == 0:
        return 0
    elif n == 1:
        memo_one[1] = 1
        return memo_one[1]
    else:
        if memo_one[n] == 0:
            memo_one[n] = fib_one(n - 2) + fib_one(n - 1)
            return memo_one[n]
        else:
            return memo_one[n]


for _ in range(T):
    temp = int(input())
    print("{} {}".format(fib_zero(temp), fib_one(temp)))
