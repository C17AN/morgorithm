from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
degree = [0] * (N + 1)

for _ in range(M):
    src, dist = map(int, input().split())
    graph[src].append(dist)
    degree[dist] += 1

q = deque()
for i in range(1, N + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    dist = q.popleft()
    print(dist, end=" ")
    for node in graph[dist]:
        degree[node] -= 1
        if degree[node] == 0:
            q.append(node)
