from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))

A.sort()


for t in target:
    if A[bisect_left(A, t)] == t:
        print(1)
    else:
        print(0)