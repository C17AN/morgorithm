from collections import deque

N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
cheezeList = [0] * 100

for row in range(N):
    temp = list(map(int, input().split()))
    for col in range(len(temp)):
        if(temp[col] == 1):
            board[row][col] = temp[col]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def checkOuterBFS(start_node):
    q = deque()
    q.append((0, 0))
    board[0][0] = -1
    outerVisited = [[False] * M for _ in range(N)]
    while q:
        node = q.popleft()
        y, x = node
        outerVisited[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if(outerVisited[ny][nx] == False):
                if(board[ny][nx] == 1):
                    continue
                else:
                    board[ny][nx] = -1
                    q.append((ny, nx))
                    outerVisited[ny][nx] = True


def meltable(node):
    meltable = False
    for i in range(4):
        ny = node[0] + dy[i]
        nx = node[1] + dx[i]
        if(board[ny][nx] == -1):
            meltable = True
    return meltable


def meltingCheezeBFS(start_node):
    q = deque()
    q.append(start_node)
    y, x = start_node
    if(meltable(start_node)):
        board[y][x] = 0
    while q:
        node = q.popleft()
        y, x = node

        visited[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if(visited[ny][nx] == False):
                if(board[ny][nx] == 1 and meltable((ny, nx))):
                    q.append((ny, nx))
                    board[ny][nx] = 0
                    visited[ny][nx] = True
    # print("cheeze melting: ", board, cnt)


def cheezeRemaining(day):
    cnt = 0
    cheezeRemain = False
    for row in range(N):
        for col in range(M):
            if(board[row][col] == 1):
                cnt += 1
                cheezeRemain = True

    cheezeList[day] = cnt
    return cheezeRemain


cnt = 0
while True:
    visited = [[False] * M for _ in range(N)]
    if(not cheezeRemaining(cnt)):
        break
    checkOuterBFS((0, 0))
    for row in range(N):
        for col in range(M):
            if(board[row][col] == 1 and visited[row][col] == False):
                meltingCheezeBFS((row, col))
    cnt += 1

print(cnt)
print(cheezeList[cnt - 1])
