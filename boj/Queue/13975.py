import sys
import heapq
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    heap = []
    cost = 0
    N = int(input())
    temp = list(map(int, input().split()))
    for elem in temp:
        heapq.heappush(heap, elem)

    for _ in range(N - 1):
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        tempCost = (one + two)
        cost += tempCost
        heapq.heappush(heap, tempCost)
    print(cost)
