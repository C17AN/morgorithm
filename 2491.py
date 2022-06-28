N = int(input())
arr = [0]
arr.extend(list(map(int, input().split())))

d = [0] * (N + 1)
maxLength = 0
increasingLength = 0
decreasingLength = 0

for i in range(1, N + 1):
    if arr[i] > arr[i - 1]:
        increasingLength += 1
        decreasingLength = 1
        if increasingLength > maxLength:
            maxLength = increasingLength

    elif arr[i] < arr[i - 1]:
        increasingLength = 1
        decreasingLength += 1
        if decreasingLength > maxLength:
            maxLength = decreasingLength

    else:
        increasingLength += 1
        decreasingLength += 1
        if increasingLength > maxLength:
            maxLength = increasingLength
        if decreasingLength > maxLength:
            maxLength = decreasingLength
print(maxLength)
