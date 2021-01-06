N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N):
    src, dist = map(int, input().split())
    graph[src][dist], graph[dist][src] = True, True


def DFS(startNode, visited):
    visited.append(startNode)
    for node in range(len(graph[startNode])):
        if graph[startNode][node] is True and (node not in visited):
            DFS(node, visited)

    return visited


print(*DFS(V, []))

print(graph)
