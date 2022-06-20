from math import ceil, floor
import sys

input = sys.stdin.readline

K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1]
mid = 0
wireCount = 0

while start <= end:
    mid = (start + end) // 2
    wireCount = 0
    for item in arr:
        wireCount += item // mid
    if wireCount >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
