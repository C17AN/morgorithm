T = int(input())

board = [list(map(int, input().split())) for _ in range(5)]
student = [0] * T

for grade in range(5):
    for row in range(T):
        for col in range(5):
            if board[row][col]
