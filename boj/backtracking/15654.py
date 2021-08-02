N, M = map(int, input().split())

numbers = list(map(int, input().split()))
visited = []
numberList = []

numbers.sort()


def backtrack(depth):
    if depth == M:
        print(*numberList)
        return

    for num in numbers:
        if num not in visited:
            visited.append(num)
            numberList.append(num)
            backtrack(depth + 1)
            visited.pop()
            numberList.pop()


backtrack(0)
