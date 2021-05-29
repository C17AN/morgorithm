N = int(input())
numList = []

numList = list(map(int, input().split()))

numList.sort()
print(numList[0], numList[N - 1])
