N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))


def binSearch(target):
    left = 0
    right = len(A) - 1
    mid = int((left + right) / 2)

    while True:
        mid = int((left + right) / 2)
        if left <= right:
            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                return 1
        else:
            return 0


for target in B:
    print(binSearch(target))
