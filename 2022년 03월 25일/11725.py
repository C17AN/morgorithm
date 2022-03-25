from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
parent = [0] * (N + 1)

for _ in range(N - 1):
    src, dist = map(int, input().split())
    graph[src].append(dist)
    graph[dist].append(src)

q = deque([1])
visited[1] = True

while q:
    dist = q.popleft()
    for node in graph[dist]:
        if visited[node] == False:
            q.append(node)
            parent[node] = dist
            visited[node] = True

for i in range(2, N + 1):
    print(parent[i])
