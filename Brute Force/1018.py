boardTypeA = [
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
]

boardTypeB = [
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
]

board = []

N, M = map(int, input().split())

for i in range(N):
    board.append(input())


def calculateDiff(row, col):
    diffA, diffB = 0, 0
    for i in range(8):
        for j in range(8):
            if board[row + i][col + j] != boardTypeA[i][j]:
                diffA += 1
            if board[row + i][col + j] != boardTypeB[i][j]:
                diffB += 1
    return min(diffA, diffB)


def setStartPoint():
    ans = 9999
    for i in range(N - 7):
        for j in range(M - 7):
            result = calculateDiff(i, j)
            if ans > result:
                ans = result
    return ans


print(setStartPoint())