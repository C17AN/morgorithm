def func4(n):
    i = 0
    while 2**i <= n:
        i += 1
    return 2**(i - 1)


print(func4(97615282))