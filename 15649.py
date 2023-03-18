N, M = map(int, input().split())

arr = [-1] * M
used = [False] * (N + 1)


def backtrack(depth):
    if (depth == M):
        for item in arr:
            print(item, end=" ")
        print()
        return

    else:
        for i in range(1, N + 1):
            if used[i] == False:
                used[i] = True
                arr[depth] = i
                backtrack(depth + 1)
                used[i] = False
                arr[depth] = -1

        return


backtrack(0)
