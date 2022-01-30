arr = []
used = [False] * 101
result = 0
found = False


def backtrack(N, cnt):
    global result
    global found
    if found == False and cnt == 7 and result == 100:
        for i in range(0, 100):
            if used[i] == True:
                print(i)
        found = True
        return
    elif cnt == 7:
        return
    else:
        for i in range(N, 9):
            if used[arr[i]] == False:
                used[arr[i]] = True
                result += arr[i]
                backtrack(i, cnt + 1)
                used[arr[i]] = False
                result -= arr[i]


for i in range(9):
    arr.append(int(input()))

arr.sort()

backtrack(0, 0)
