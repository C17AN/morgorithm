import sys

input = sys.stdin.readline

N = int(input())
arr = [0]
arr.extend(list(map(int, input().split())))

M = int(input())


for i in range(1, N + 1):
    arr[i] = arr[i - 1] + arr[i]

for i in range(M):
    i, j = map(int, input().split())
    print(arr[j] - arr[i - 1])
