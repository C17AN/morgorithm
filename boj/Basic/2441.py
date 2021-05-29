N = int(input())
for level in range(N):
    for _ in range(N - level):
        print('*', end='')
    print()