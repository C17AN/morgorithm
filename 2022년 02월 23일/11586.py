N = int(input())
arr = []

for i in range(N):
    temp = list(input())
    arr.append(temp)

K = int(input())

if K == 1:
    for row in range(N):
        for col in range(N):
            print(arr[row][col], end="")
        print()
elif K == 2:
    for row in range(N):
        for col in range(N - 1, -1, -1):
            print(arr[row][col], end="")
        print()
elif K == 3:
    for row in range(N - 1, -1, -1):
        for col in range(N):
            print(arr[row][col], end="")
        print()
