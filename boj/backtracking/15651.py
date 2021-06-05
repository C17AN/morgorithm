N, M = map(int, input().split())

numberList = []


def backTrack(depth):
    if depth == M:
        print(*numberList)
        return
    for i in range(1, N + 1):
        numberList.append(i)
        backTrack(depth + 1)
        numberList.pop()


backTrack(0)
