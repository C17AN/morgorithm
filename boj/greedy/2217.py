T = int(input())

ropeList = []
maxWeight = 0

for _ in range(T):
    ropeList.append(int(input()))

ropeList.sort()

for ropeCount in range(T):
    tempWeight = ropeList[ropeCount] * (T - ropeCount)
    maxWeight = tempWeight if tempWeight > maxWeight else maxWeight

print(maxWeight)
