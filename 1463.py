X = int(input())
table = [0] * 1000001


for i in range(2, X + 1):
    table[i] = table[i - 1] + 1
    if i % 3 == 0:
        table[i] = min(table[i], table[i // 3] + 1)
    if i % 2 == 0:
        table[i] = min(table[i], table[i // 2] + 1)


print(table[X])
