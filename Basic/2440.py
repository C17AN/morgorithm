N = int(input())
for level in range(1, N + 1):
    for _ in range(N - level):
        print(' ', end='')
    for _ in range(level):
        print('*', end='')
    print()