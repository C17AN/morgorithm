N = int(input())

graph = [[] i in range(N)]

for _ in range(N):
    src, dest = map(int, input().split())
    graph[src].append(dest)
    graph[dest].append(src)
    print(graph)

print(graph)