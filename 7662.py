from heapq import heappop, heappush, heapify
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    minHeap, maxHeap = [], []
    k = int(input())
    used = [False] * 1000001

    for i in range(k):
        command, value = input().split()
        if command == "I":
            heappush(minHeap, (int(value), i))
            heappush(maxHeap, (-int(value), i))
            used[i] = True
        else:
            if value == "1":
                while maxHeap and not used[maxHeap[0][1]]:
                    heappop(maxHeap)
                if maxHeap:
                    used[maxHeap[0][1]] = False
                    heappop(maxHeap)
            elif value == "-1":
                while minHeap and not used[minHeap[0][1]]:
                    heappop(minHeap)
                if minHeap:
                    used[minHeap[0][1]] = False
                    heappop(minHeap)

    while maxHeap and not used[maxHeap[0][1]]:
        heappop(maxHeap)
    while minHeap and not used[minHeap[0][1]]:
        heappop(minHeap)

    if minHeap and maxHeap:
        print(-maxHeap[0][0], minHeap[0][0])
    else:
        print("EMPTY")
