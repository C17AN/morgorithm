import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
weightList = [[INF] * (N + 1) for _ in range(N + 1)]
visited = [[0] * (N + 1) for _ in range(N + 1)]
heap = []

for i in range(M):
    src, dist, weight = map(int, input().split())
    graph[src].append((dist, weight))
    graph[dist].append((src, weight))


def dijkstra(startNode):
    weightList[startNode][startNode] = 0
    heapq.heappush(heap, (0, startNode))

    while heap:
        weight, current = heapq.heappop(heap)
        if weightList[startNode][current] < weight:
            continue

        for _next, _weight in graph[current]:
            nextWeight = weight + _weight
            if nextWeight < weightList[startNode][_next]:
                weightList[startNode][_next] = nextWeight
                heapq.heappush(heap, (nextWeight, _next))
                visited[_next][startNode] = current


for i in range(1, N + 1):
    dijkstra(i)

for row in range(1, N + 1):
    for col in range(1, N + 1):
        if visited[row][col] == 0:
            print("-", end=" ")
        else:
            print(visited[row][col], end=" ")
    print()
