import sys
from collections import deque

input = sys.stdin.readline

N,M,V = map(int,input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
dfsVisited = [False] * (N + 1)
bfsVisited = [False] * (N + 1)

for i in range(M):
    start, end = map(int, input().split())
    graph[start][end] = graph[end][start] = True

def dfs(V):
    dfsVisited[V] = True
    print(V, end=" ")

    for i in range(1, N + 1):
        if graph[V][i] == True and dfsVisited[i] == False:
            dfs(i)

def bfs():
    bfsVisited[V] = True
    q = deque([V])
    print(V, end=' ')   
    while q:
        n = q.popleft()
        for i in range(1, N + 1):
            if graph[n][i] == True and bfsVisited[i] == False:
                q.append(i)
                bfsVisited[i] = True
                print(i, end=' ')


dfs(V)
print()
bfs()

