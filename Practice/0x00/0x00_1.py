def func1(n):
    sum = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


print(func1(34567))
