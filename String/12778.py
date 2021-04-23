T = int(input())

for i in range(T):
    M, case = input().split()
    data = list(input().split())
    for i in range(len(data)):
        if case == 'C':
            data[i] = ord(data[i]) - 64
        elif case == 'N':
            data[i] = chr(int(data[i]) + 64)
    print(*data)