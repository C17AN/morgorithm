N = int(input())

for level in range(0, N):
    for space in range(N - level - 1):
        print(' ', end="")
    for star in range(level * 2 + 1):
        print('*', end="")
    print()