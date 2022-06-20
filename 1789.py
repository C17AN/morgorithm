N = int(input())

left = 0
right = N
count = 0
while 1:
    if left > right:
        break
    mid = (left + right) // 2
    temp = sum(range(1, mid + 1))
    print(temp)
    if temp <= N:
        count = mid
        left = mid + 1
    else:
        right = mid - 1

print(count)
