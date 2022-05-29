import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

visitedA = [[-1] * C for _ in range(R)]
visitedB = [[-1] * C for _ in range(R)]
visitedC = [[-1] * C for _ in range(R)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
minRoute = 1e9
minCount = 0
board = []

for _ in range(R):
    board.append(list(input()))

Ay, Ax = map(int, input().split())
By, Bx = map(int, input().split())
Cy, Cx = map(int, input().split())


def bfs(startNode, villianType):
    q = deque()
    y, x = startNode
    if villianType == 'A':
        visitedA[y - 1][x - 1] = 0
    elif villianType == 'B':
        visitedB[y-1][x-1] = 0
    elif villianType == 'C':
        visitedC[y-1][x-1] = 0
    q.append((y - 1, x - 1))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if villianType == 'A':
                    if visitedA[ny][nx] == -1 and board[ny][nx] == '0':
                        q.append((ny, nx))
                        visitedA[ny][nx] = visitedA[y][x] + 1
                elif villianType == 'B':
                    if visitedB[ny][nx] == -1 and board[ny][nx] == '0':
                        q.append((ny, nx))
                        visitedB[ny][nx] = visitedB[y][x] + 1
                elif villianType == 'C':
                    if visitedC[ny][nx] == -1 and board[ny][nx] == '0':
                        q.append((ny, nx))
                        visitedC[ny][nx] = visitedC[y][x] + 1


bfs((Ay, Ax), 'A')
bfs((By, Bx), 'B')
bfs((Cy, Cx), 'C')


for row in range(R):
    for col in range(C):
        if visitedA[row][col] > -1 and visitedB[row][col] > -1 and visitedC[row][col] > -1:
            temp = max(visitedA[row][col],
                       visitedB[row][col], visitedC[row][col])
            if minRoute > temp:
                minRoute = temp
                minCount = 1
            elif minRoute == temp:
                minCount += 1

if minCount != 0:
    print(minRoute)
    print(minCount)
else:
    print(-1)
