N, K = map(int, input().split())
arr = list(map(int, input().split()))
accSum = [0] * (N + 1)
maxValue = -99999

for i in range(1, N + 1):
    accSum[i] = accSum[i - 1] + arr[i - 1]

for i in range(N - K + 1):
    maxValue = max(maxValue, accSum[i + K] - accSum[i])

print(maxValue)
