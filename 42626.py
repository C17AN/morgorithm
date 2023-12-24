import heapq

def solution(scoville, K):
    heap = []
    count = 0
    for value in scoville:
        heapq.heappush(heap, value)
    while True:
        minValue = heapq.heappop(heap)
        if(minValue < K):
            if(len(heap) == 0):
                return -1
            heapq.heappush(heap, minValue + heapq.heappop(heap) * 2)
            count += 1
        else:
            break
    print(count)
    return count
        
solution([5,2], 20)