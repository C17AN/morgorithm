def DFS(adj, s):
    tovisit = [s]
    visited = []
    while tovisit:
        u = tovisit.pop()
        visited.append(u)
        for v in adj[u]:
            if v not in visited + tovisit:
                tovisit.append(v)
    return visited


G1 = {
    1: [2, 3],
    2: [3, 4, 5],
    3: [5, 7, 8],
    4: [5],
    5: [6],
    6: [],
    7: [8],
    8: []
}
print(DFS(G1, 1))
