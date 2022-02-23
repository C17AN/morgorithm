def getNumberFromList(arr):
    number = ''
    for char in arr:
        number += str(char)
    return int(number)


T = int(input())

for _ in range(T):
    count = 0
    N, M = map(int, input().split())
    X = getNumberFromList(list(map(int, input().split())))
    Y = getNumberFromList(list(map(int, input().split())))
    board = list(map(int, input().split()))
    for i in range(N):
        value = getNumberFromList(board[i: i + M])
        if i + M > N:
            value = int(str(getNumberFromList(
                board[i: i + M])) + str(getNumberFromList(board[0: i + M - N])))

        if X < value < Y:
            count += 1
    print(count)
