from collections import deque

dy = [-1, 0, 1, 0, -1, 1, 1, -1]
dx = [0, 1, 0, -1, 1, 1, -1, -1]


def BFS(node):
    q = deque()
    q.append(node)
    global visited
    visited[node[0]][node[1]] = True

    while q:
        y, x = q.pop()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < h and 0 <= nx < w:
                if visited[ny][nx] == False and board[ny][nx] == 1:
                    q.append((ny, nx))
                    visited[ny][nx] = True


while 1:
    w, h = map(int, input().split())
    visited = [[False] * w for _ in range(h)]
    board = []
    cnt = 0

    if w == 0 and h == 0:
        break

    for _ in range(h):
        board.append(list(map(int, input().split())))

    for row in range(h):
        for col in range(w):
            if board[row][col] == 1 and visited[row][col] == False:
                BFS((row, col))
                cnt += 1

    print(cnt)
    cnt = 0
