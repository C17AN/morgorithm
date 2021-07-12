N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

leftPointer = 0
rightPointer = 0

while rightPointer <= len(arr):
    tempSum = 0
    if(sum(arr[leftPointer: rightPointer]) < M):
        rightPointer += 1
    elif(sum(arr[leftPointer: rightPointer]) > M):
        leftPointer += 1
    else:
        ans += 1
        rightPointer += 1

print(ans)
