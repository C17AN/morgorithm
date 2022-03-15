R, C, N = map(int, input().split())

board = [list(input()) for _ in range(R)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

visited = [[False] * C for _ in range(R)]
reserved = [[False] * C for _ in range(R)]

for second in range(1, N + 1):
    if second % 2 == 0:
        visited = [[False] * C for _ in range(R)]
        reserved = [[False] * C for _ in range(R)]
    for row in range(R):
        for col in range(C):
            if second % 2 == 0:
                if board[row][col] == ".":
                    board[row][col] = "O"
                else:
                    reserved[row][col] = True
            else:
                if reserved[row][col] == True and visited[row][col] == False:
                    board[row][col] = "."
                    for i in range(4):
                        ny = row + dy[i]
                        nx = col + dx[i]
                        if 0 <= ny < R and 0 <= nx < C:
                            if board[ny][nx] == "O":
                                board[ny][nx] = "."

for row in range(R):
    for col in range(C):
        print(board[row][col], end="")
    print()
