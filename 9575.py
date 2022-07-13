def isLuckyNumber(number):
    temp = number
    if number in isUsed:
        return False
    while number >= 10:
        if number % 10 != 5 and number % 10 != 8:
            return False
        number //= 10
    if number != 5 and number != 8:
        return False
    isUsed.append(temp)
    return True


T = int(input())
for _ in range(T):
    isUsed = []
    luckyNumberCount = 0
    N = int(input())
    A = list(map(int, input().split()))
    N = int(input())
    B = list(map(int, input().split()))
    N = int(input())
    C = list(map(int, input().split()))
    for a in A:
        for b in B:
            for c in C:
                if isLuckyNumber(a + b + c):
                    luckyNumberCount += 1
    print(luckyNumberCount)
