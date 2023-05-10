N = int(input())
operators = input().split()
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
isNumberUsed = [False] * 10


def backtrack(depth, s):
    if depth == N:
        print(s)
        return

    for i in range(10):
        if isNumberUsed[i] == False:
            if depth == 0 or (operators[depth] == "<" and i < int(s[-1])):
                isNumberUsed[i] = True
                backtrack(depth + 1, str(s) + str(i))
                isNumberUsed[i] = False
            if depth == 0 or (operators[depth] == ">" and i > int(s[-1])):
                isNumberUsed[i] = True
                backtrack(depth + 1, str(s) + str(i))
                isNumberUsed[i] = False


backtrack(0, 0)
