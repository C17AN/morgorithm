N = int(input())

for level in range(1, N + 1):
    for idx in range(N - level):
        print(' ', end='')
    for idx in range(level):
        print('*', end=' ')
    print()
