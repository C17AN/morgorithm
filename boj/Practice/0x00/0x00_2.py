def func2(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == 100:
                return 1
    return 0


print(func2(arr, 4))