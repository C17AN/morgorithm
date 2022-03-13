N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
prev = 0

while True:
    mid = int((left + right) / 2)
    if prev == mid:
        print(int(mid))
        break

    cutTreeSum = 0
    for tree in trees:
        temp = tree - mid
        if temp < 0:
            continue
        else:
            cutTreeSum += temp
    prev = mid

    if cutTreeSum < M:
        right = mid - 1
    elif cutTreeSum > M:
        left = mid + 1
    else:
        print(int(mid))
        break
