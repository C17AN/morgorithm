import heapq
import sys

input = sys.stdin.readline

pq = []
cnt = 0

N = int(input())
G = -int(input())

for i in range(1, N):
    temp = int(input())
    heapq.heappush(pq, -temp)

while True and pq:
    temp = heapq.heappop(pq)
    if temp <= G:
        temp += 1
        cnt += 1
        G -= 1
        heapq.heappush(pq, temp)
    else:
        break

print(cnt)
