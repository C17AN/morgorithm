from collections import deque

N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]


for i in range(1, M + 1):
    src, dist = map(int, input().split())
    graph[src][dist] = True
    graph[dist][src] = True

visited = [False] * (N + 1)

# 재귀 방식의 DFS


def DFS(start):
    visited[start] = True
    print(start, end=' ')
    for i in range(1, N + 1):
        if graph[start][i] == True and visited[i] == False:
            DFS(i)


DFS(V)
print()


queue = deque([])
visited = [False] * (N + 1)


def BFS(start):
    queue = deque([start])
    print(start, end=' ')
    visited[start] = True
    while queue:
        _start = queue.popleft()
        for i in range(1, N + 1):
            if graph[_start][i] == True and visited[i] == False:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')


BFS(V)


# 1 1 1
# 1 1
