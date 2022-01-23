N, M = map(int, input().split())

A = list(map(int, input().split()))
cnt = 0

left = 0
right = 0

while right <= len(A):

    if sum(A[left: right]) < M:
        right += 1
    elif sum(A[left: right]) > M:
        left += 1
    else:
        cnt += 1
        right += 1

print(cnt)
