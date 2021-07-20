import sys
import heapq
INF = sys.maxsize

input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())

weightList = [INF] * (V + 1)
heap = []  # 다음에 방문할 가중치를 저장함
graph = [[] for _ in range(V + 1)]  # 전체 그래프의 행렬


for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


def dijkstra(startNode):
    weightList[startNode] = 0
    heapq.heappush(heap, (0, startNode))

    while heap:
        weight, current = heapq.heappop(heap)
        if weightList[current] < weight:
            continue

        for _weight, _node in graph[current]:
            nextWeight = weight + _weight
            if nextWeight < weightList[_node]:
                weightList[_node] = nextWeight
                heapq.heappush(heap, (nextWeight, _node))


dijkstra(K)

for i in range(1, V + 1):
    if weightList[i] != INF:
        print(weightList[i])
    else:
        print("INF")
