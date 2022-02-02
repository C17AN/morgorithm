N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

index = 0

for number in B:
    while number >= A[index] and index < len(A) - 1:
        index += 1
    # print(A, A[index], index, number)
    if index == len(A) - 1:
        A.append(number)
    else:
        A.insert(index, number)


print(*A)
