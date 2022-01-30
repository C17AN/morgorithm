from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    temp = int(input())
    if temp:
        heappush(pq, temp)
    else:
        if pq:
            print(heappop(pq))
        else:
            print(0)
