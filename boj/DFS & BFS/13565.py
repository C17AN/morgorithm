from collections import deque

N, M = map(int, input().split())

board = []
visited = [[False] * M for _ in range(N)]
flag = False

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def BFS(node):
    q = deque()
    q.append(node)
    visited[node[0]][node[1]] = True
    global flag
    while q:
        y, x = q.popleft()
        if y == N - 1:
            flag = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == '0' and visited[ny][nx] == False:
                    q.append((ny, nx))
                    visited[ny][nx] = True

    return


for i in range(N):
    board.append(input())

for i in range(M):
    if board[0][i] == '0' and visited[0][i] == False:
        BFS((0, i))

if flag == True:
    print("YES")
else:
    print("NO")