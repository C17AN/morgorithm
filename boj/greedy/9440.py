def sortArray(arr):
    if arr[0] == 0:
        for i in range(len(arr)):
            if arr[i] != 0:
                temp = arr[i]
                arr[0] = temp
                arr[i] = 0
                break
    return arr


def concatArrayElement(arr):
    digit = 1
    result = 0
    for i in range(len(arr) - 1, -1, -1):
        result += arr[i] * digit
        digit *= 10
    return result


while True:
    A = []
    B = []
    numbers = list(map(int, input().split()))
    N = numbers.pop(0)
    if N == 0:
        break
    numbers.sort()
    while numbers:
        A.append(numbers.pop())
        if not numbers:
            break
        B.append(numbers.pop())
    A.reverse()
    B.reverse()
    A = sortArray(A)
    B = sortArray(B)
    if len(A) > len(B) and A[0] > B[0]:
        temp = B[0]
        B[0] = A[0]
        A[0] = temp
    print(concatArrayElement(A) + concatArrayElement(B))
