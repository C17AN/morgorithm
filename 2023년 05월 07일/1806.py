N, S = map(int, input().split())
numberList = list(map(int, input().split()))

startIndex = 0
endIndex = 0
accSum = 0
minLength = 0

while startIndex <= endIndex:
    accSum = accSum + numberList[endIndex]
    print(accSum)

    if accSum >= S:
        if endIndex - startIndex <= minLength:
            minLength = endIndex - startIndex

        accSum -= numberList[startIndex]
        startIndex += 1

    else:
        if endIndex == N - 1:
            startIndex += 1
            endIndex += 1

        else:
            endIndex += 1

print(minLength)
