arr = []
found = False

for _ in range(9):
    arr.append(int(input()))

result = sum(arr)

for i in range(9):
    for j in range(9):
        first, second = arr[i], arr[j]
        if i == j or found == True:
            continue
        if result - first - second == 100:
            arr.pop(arr.index(first))
            arr.pop(arr.index(second))
            found = True
            for number in sorted(arr):
                print(number)
