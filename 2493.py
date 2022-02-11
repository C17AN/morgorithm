N = int(input())
arr = list(map(int, input().split()))
s = []

for index in range(len(arr)):
    # print(s)
    while s:
        if s[-1][1] > arr[index]:
            print(s[-1][0], end=" ")
            break
        else:
            s.pop()

    if not s:
        print(0, end=' ')

    s.append((index + 1, arr[index]))
