board = [[0] * 101 for _ in range(101)]

for i in range(4):
    lx, ly, rx, ry = map(int, input().split())
    for row in range(ry - ly):
        for col in range(rx - lx):
            board[row + ly][col + lx] = 1

size = 0

for row in range(101):
    for col in range(101):
        size += board[row][col]

print(size)
