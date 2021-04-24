M, N = map(int, input().split())
apart = []
blind = [0, 0, 0, 0, 0]


def checkBlind(M, N):
    global blind
    cnt = 0
    for row in range(4):
        for col in range(4):
            if apart[M + row][N + col] == '*':
                cnt += 1

    if cnt == 0:
        blind[0] += 1
    elif cnt == 4:
        blind[1] += 1
    elif cnt == 8:
        blind[2] += 1
    elif cnt == 12:
        blind[3] += 1
    elif cnt == 16:
        blind[4] += 1


for _ in range(M * 5 + 1):
    apart.append(input())

for row in range(1, M * 5 + 1, 5):
    for col in range(1, N * 5 + 1, 5):
        checkBlind(row, col)

print(*blind)
