from heapq import heapify, heappop, heappush
from collections import deque


def solution(operations):
    minHeap = []
    maxHeap = []
    heapify(minHeap)
    heapify(maxHeap)

    for operation in operations:
        command, number = operation.split(" ")
        if command == "I":
            heappush(minHeap, number)
            heappush(maxHeap, (-int(number), int(number)))
        else:
            if minHeap or maxHeap:
                if number == '-1':
                    print("min pop, ", number, heappop(minHeap))
                else:
                    print("max pop, ", number, heappop(maxHeap)[1])

    print(minHeap, maxHeap)
    return [maxHeap[-1][1], minHeap[0]]


print(solution(["I -45", "I 653", "D 1", "I -642",
                "I 45", "I 97", "D 1", "D -1", "I 333"]))

# ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
