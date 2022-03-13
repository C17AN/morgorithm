from collections import deque

N = int(input())
counts = list(map(int, input().split()))
tempList = []
for i in range(1, N + 1):
    tempList.append((i, counts[i - 1]))
balloons = deque(tempList)

index, count = balloons.popleft()
print(index, end=" ")

while balloons:
    if count > 0:
        for i in range(count - 1):
            temp = balloons.popleft()
            balloons.append(temp)
        index, count = balloons.popleft()

    else:
        for i in range(abs(count) - 1):
            temp = balloons.pop()
            balloons.appendleft(temp)
        index, count = balloons.pop()
    print(index, end=" ")
