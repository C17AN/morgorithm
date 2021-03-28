from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = []

for _ in range(N):
    src, dist = map(int, input().split())
    graph[src][dist], graph[dist][src] = True, True


def DFS(start_node):
    visited[start_node] = True
    print(start_node, end=" ")
    for i in range(1, N + 1):
        if visited[i] == False and graph[start_node][i] == True:
            DFS(start_node)


print(graph)
print(DFS(1))
