N, X = map(int, input().split())
A = [0]
A.extend(map(int, input().split()))
S = [0] * N

left = 0
right = 0
maxValueCount = 1
maxValue = A[0]

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
            # print("res: ", tempSum, i)
            maxValue = tempSum
            maxValueCount = 1
        elif tempSum == maxValue:
            maxValueCount += 1
            # print("res: ", tempSum, i)

    if maxValue == 0:
        print("SAD")
    else:
        print(maxValue)
        print(maxValueCount)

# print(A)
