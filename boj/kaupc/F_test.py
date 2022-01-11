arr = [[1, 2, 3, 4, 5],
      [1, 2, 3, 4, 5],
      [1, 2, 3, 4, 5]]

# for i in zip(*input_val):
#   print(i)
# print([sum(x) for x in zip(*input_val)])
# score = list(map(sum, zip(*arr)))
# print(score)


def diagonalsum(m):
    return sum(m[i][i] for i in range(len(m)))

print(diagonalsum(arr))