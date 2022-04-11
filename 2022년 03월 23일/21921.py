N, X = map(int, input().split())
A = [0]
A.extend(map(int, input().split()))

maxValueCount = 0
maxValue = 0

for i in range(1, N + 1):
    A[i] = A[i - 1] + A[i]

if N == X:
    if A[N] == 0:
        print("SAD")
    else:
        print(A[N])
        print(1)

else:
    for i in range(X - 1, N + 1):
        tempSum = A[i] - A[i - X]
        if tempSum > maxValue:
            maxValue = tempSum
            maxValueCount = 1
        elif tempSum == maxValue:
            maxValueCount += 1

    if maxValue == 0:
        print("SAD")
    else:
        print(maxValue)
        print(maxValueCount)
