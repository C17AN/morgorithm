N = int(input())
left = 0
right = N
prev = -1

while True:
    mid = (left + right) // 2
    if mid ** 2 == N:
        print(mid)
        break
    elif mid == prev:
        print(mid + 1)
        break
    elif mid ** 2 < N:
        left = mid + 1
    elif mid ** 2 > N:
        right = mid - 1
    prev = mid
