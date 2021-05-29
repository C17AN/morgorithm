T = int(input())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def DFS(row, col, visited):
    for i in range(4):
        new_row = row + dy[i]
        new_col = col + dx[i]
        if field[new_row][new_col] == 1 and visited[new_row][new_col] == False:
            visited[new_row][new_col] = True
            DFS(new_row, new_col, visited)


for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    visited = [[False for _ in range(M + 1)] for _ in range(N + 1)]
    cnt = 0

    for i in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    for col in range(M):
        for row in range(N):
            if field[row][col] == 1 and visited[row][col] == False:
                cnt += 1
                DFS(row, col, visited)

    print(cnt)