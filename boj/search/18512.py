X, Y, P1, P2 = map(int, input().split())

found = False
visited = [{"p1": False, "p2": False} for _ in range(10001)]

for i in range(P1, 10001, X):
    visited[i]['p1'] = True

for i in range(P2, 10001, Y):
    visited[i]['p2'] = True

for point in range(1, 10001):
    if visited[point]['p1'] == True and visited[point]['p2'] == True:
        found = True
        break

if found == False:
    print(-1)
