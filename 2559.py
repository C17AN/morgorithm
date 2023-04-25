N, K = map(int, input().split())
arr = list(map(int, input().split()))
accSumList = [0] * (N + 1)
maxValue = -99999

for index in range(1, N + 1):
    accSumList[index] = accSumList[index - 1] + arr[index - 1]

for index in range(N - K + 1):
    maxValue = max(maxValue, accSumList[index + K] - accSumList[index])

print(maxValue)
