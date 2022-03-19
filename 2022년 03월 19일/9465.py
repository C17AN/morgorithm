T = int(input())
for _ in range(T):
    n = int(input())
    stickers = []
    d = [[0] * (n + 1) for _ in range(2)]
    for _ in range(2):
        stickers.append(list([0, *map(int, input().split())]))
    d[0][0], d[1][0] = 0, 0
    d[0][1] = stickers[0][1]
    d[1][1] = stickers[1][1]
    for col in range(2, n + 1):
        d[0][col] = max(d[1][col - 1], d[1][col - 2]) + stickers[0][col]
        d[1][col] = max(d[0][col - 1], d[0][col - 2]) + stickers[1][col]
    # print(d)
    print(max(d[0][n], d[1][n]))
