import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
accSumList = [0]

for index, number in enumerate(numbers):
    accSumList.append(accSumList[-1] + number)

for _ in range(M):
    i, j = map(int, input().split())
    print(accSumList[j] - accSumList[i - 1])
