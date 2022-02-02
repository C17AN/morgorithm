N, M = map(int, input().split())
minPackagePrice, minSinglePrice = 1001, 1001
priceSum = 0

for i in range(M):
    packagePrice, singlePrice = map(int, input().split())
    minPackagePrice = packagePrice if minPackagePrice > packagePrice else minPackagePrice
    minSinglePrice = singlePrice if minSinglePrice > singlePrice else minSinglePrice


while N > 0:
    if N >= 6:
        if minSinglePrice * N > minPackagePrice * (N // 6):
          priceSum += minSinglePrice * N
          N = 0
        else:
          priceSum += minPackagePrice * (N // 6)
          N -= 6
    else:
        if minSinglePrice * N < minPackagePrice:
            priceSum += minSinglePrice * N
            N = 0
        else:
            priceSum += minPackagePrice
            N -= 6

print(priceSum)
