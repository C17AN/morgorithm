from collections import deque

N, M, V = map(int, input().split())

graph = [[0] for i in range(10001)]
dfs_ans = []
bfs_ans = []

for i in range(M):
    src, dist = map(int, input().split())
    graph[src].append(dist)
    graph[dist].append(src)

for i in range(N):
    graph[i].sort()


def DFS(start_node, visited):
    visited.append(start_node)
    dfs_ans.append(start_node)
    node_graph = graph[start_node]
    for i in node_graph[1:]:
        if i not in visited:
            DFS(i, visited)


def BFS(start_node):
    visited = []
    queue = deque()
    queue.append(start_node)
    visited.append(start_node)
    bfs_ans.append(start_node)

    while len(queue) != 0:
        next_node = queue.popleft()
        node_graph = graph[next_node]
        for i in node_graph[1:]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
                bfs_ans.append(i)


DFS(V, [])
BFS(V)

if len(dfs_ans) > 1:
    print(*dfs_ans)
    print(*bfs_ans)