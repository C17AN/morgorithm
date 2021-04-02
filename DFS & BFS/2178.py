from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def BFS(start_node):
    y, x = start_node
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True
    count = 0

    while len(queue) != 0:
        curY, curX = queue.popleft()
        for i in range(4):
            nextY = curY + dy[i]
            nextX = curX + dx[i]
            if 0 <= nextY < N and 0 <= nextX < M:
                if visited[nextY][nextX] == False and maze[nextY][nextX] != 0:
                    visited[nextY][nextX] = True
                    queue.append((nextY, nextX))
                    maze[nextY][nextX] = maze[curY][curX] + 1


BFS((0, 0))
print(maze[N - 1][M - 1])
