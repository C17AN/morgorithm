# from queue import PriorityQueue
import heapq

N = int(input())
pq = []
for i in range(1, N + 1):
    S, C, L = map(int, input().split())
    # q.put((-S, C, L, i))
    heapq.heappush(pq, (-S, C, L, i))

print(heapq.heappop(pq)[3])
