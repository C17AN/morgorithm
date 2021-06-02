import copy
from collections import deque
N, M = map(int, input().split())

board = []
originalBoard = []
visited = [[False] * M for _ in range(N)]
max_cnt = 0

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def BFS(node):
    global max_cnt
    global visited
    q = deque()
    q.append(node)
    cnt = 1
    visited[node[0]][node[1]] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:

                if board[ny][nx] == 2:
                    return 0
                # if board[0][4] == 1 and board[1][3] == 1 and board[3][3] == 1:
                #     print(y, x, node, cnt)
                if visited[ny][nx] == False and board[ny][nx] == 0:
                    if max_cnt == 0:
                        print("line 31 ", "start: ", node, (ny, nx), cnt)
                        if board[ny][nx] == 2:
                            print('line 33', 'return')
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    cnt += 1
    if max_cnt == 0:
        print("line 41 ", cnt)
    return cnt


def installFence(depth):
    global board
    global visited
    global max_cnt
    cnt = 0
    # 종료조건
    if depth == 2:
        for row in range(N):
            for col in range(M):
                if board[row][col] == 0 and visited[row][col] == False:
                    cnt += BFS((row, col))

        if cnt > max_cnt:
            print("line 58 ", board, cnt)
            max_cnt = cnt

        visited = [[False] * M for _ in range(N)]

        return

    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                board[row][col] = 1
                installFence(depth + 1)
                board[row][col] = 0


# 입력
for i in range(N):
    originalBoard.append(list(map(int, input().split())))

board = copy.deepcopy(originalBoard)

for row in range(N):
    for col in range(M):
        if board[row][col] == 0:
            board[row][col] = 1
            installFence(0)
            board = copy.deepcopy(originalBoard)

print(max_cnt)