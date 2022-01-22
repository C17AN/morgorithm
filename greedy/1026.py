T = int(input())

S = 0
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
for i in range(T):
    tempMax = max(B)
    S += tempMax * A[i]
    B.remove(tempMax)

print(S)
