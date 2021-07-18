import heapq
import sys

input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    temp = int(input())
    heapq.heappush(heap, (-temp, temp))
    if temp == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
