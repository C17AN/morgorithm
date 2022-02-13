arr = [list(map(int, input().split())) for _ in range(9)]

maxValue = 0
maxRow, maxCol = 0, 0

for row in range(9):
    for col in range(9):
        if arr[row][col] >= maxValue:
            maxValue = arr[row][col]
            maxRow, maxCol = row, col

print(maxValue)
print(maxRow + 1, maxCol + 1)
