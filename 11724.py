from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0


for i in range(1, N + 1):
    q = deque()
    q.append(i)
    if visited[i] == False:
        visited[i] = True
        count += 1
        while q:
            dist = q.popleft()
            for node in graph[dist]:
                if visited[node] == False:
                    q.append(node)
                    visited[node] = True

print(count)
