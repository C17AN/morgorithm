N = int(input())


def checkNumber(N):
    flag = True
    while N:
        value = N % 10
        N //= 10
        if value != 4 and value != 7:
            flag = False

    return flag


for i in range(N, 0, -1):
    if checkNumber(i) == True:
        print(i)
        break
