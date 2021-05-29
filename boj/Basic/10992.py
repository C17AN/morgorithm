N = int(input())

for level in range(1, N + 1):
    for idx in range(N - level):
        print(' ', end="")
    for idx in range(level * 2 - 1):
        if level != N:
            if idx == 0 or idx == level * 2 - 2:
                print('*', end='')
            else:
                print(' ', end='')
        else:
            print('*', end='')
    print()
