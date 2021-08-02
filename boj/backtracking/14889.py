import sys

input = sys.stdin.readline
N = int(input())

board = []
used = [False] * N

start = 0
link = 0
minDiff = 999

for _ in range(N):
    board.append(list(map(int, input().split())))


def calculate():
    global start
    global link
    for i in range(N - 1):
        for j in range(i, N):
            if used[i] == True and used[j] == True:
                start += board[i][j]
                start += board[j][i]
            elif used[i] == False and used[j] == False:
                link += board[i][j]
                link += board[j][i]


def backtrack(player, depth):
    global score
    global start
    global link
    global minDiff
    if depth == N // 2:
        calculate()
        if abs(start - link) < minDiff:
            minDiff = abs(start - link)
        if(minDiff == 0):
            print(minDiff)
            exit()
        start = 0
        link = 0
        return

    for i in range(player + 1, N):
        if used[i] == False:
            used[i] = True
            backtrack(i, depth + 1)
            used[i] = False


for player in range(N):
    used[player] = True
    backtrack(player, 1)
    used[player] = False

print(minDiff)
