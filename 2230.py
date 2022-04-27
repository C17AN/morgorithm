import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort()

left = 0
right = 0
ans = 9999999999999

while right < N:
    temp = arr[right] - arr[left]
    if temp < M:
        right += 1
    elif temp > M:
        left += 1
        if temp < ans:
            ans = temp
    elif temp == M:
        ans = temp
        break

print(ans)
