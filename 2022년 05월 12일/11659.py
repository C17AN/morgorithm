N, M = map(int, input().split())
arr = list(map(int, input().split()))
accSum = [0] * (N + 1)
accSum[1] = arr[0]

for arrIndex in range(1, len(arr) + 1):
    accSum[arrIndex] = accSum[arrIndex - 1] + arr[arrIndex - 1]

# print(accSum)

for i in range(M):
    i, j = map(int, input().split())
    print(accSum[j] - accSum[i - 1])
