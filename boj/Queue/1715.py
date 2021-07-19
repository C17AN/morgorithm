import sys
import heapq

N = int(input())
heap = []
count = 0
tempCount = 0

for _ in range(N):
    temp = int(input())
    heapq.heappush(heap, temp)

for _ in range(N - 1):
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    tempCount = one + two
    heapq.heappush(heap, tempCount)
    count += tempCount


print(count)
