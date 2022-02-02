N = int(input())


def recursive(N):
    if N <= 1:
        return 1
    return N * recursive(N - 1)


ans = recursive(N)
print(ans)
