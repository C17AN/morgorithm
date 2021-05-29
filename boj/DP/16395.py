N, K = map(int, input().split())

triangle = [[1], [1, 1]]

for level in range(2, N):
    row = []
    for i in range(1, level):
        temp = triangle[level - 1][i - 1] + triangle[level - 1][i]
        row.append(temp)
    triangle.append([1] + row + [1])

print(triangle[N - 1][K - 1])
