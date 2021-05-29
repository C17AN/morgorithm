N, M = map(int, input().split())
number_list = [0] * (N + 1)
visited = [False] * (N + 1)


def backTrack(depth):
    if depth == M:
        print(*number_list)
        return

    for i in range(1, N + 1):
        if i not in visited:
            visited[i] = True
            number_list[depth] = i
            backTrack(depth + 1)
            visited[i] = False


backTrack(0)