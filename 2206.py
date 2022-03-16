from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def BFS(startNode):
    y, x = startNode
    q = deque()
    q.append((y, x, 0))
    visited[y][x][0] = 1

    while q:
        y, x, status = q.popleft()
        if y == N - 1 and x == M - 1:
            return visited[y][x][status]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == 0 and visited[ny][nx][status] == 0:
                    visited[ny][nx][status] = visited[y][x][status] + 1
                    q.append((ny, nx, status))

                if board[ny][nx] == 1 and status == 0 and visited[ny][nx][status] == 0:
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    q.append((ny, nx, 1))

    return -1


print(BFS((0, 0)))
