import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
accSum = [0] * (N + 1)

for i in range(1, N + 1):
    accSum[i] = accSum[i - 1] + arr[i - 1]

for _ in range(Q):
    start, end = map(int, input().split())
    print(accSum[end] - accSum[start - 1])
