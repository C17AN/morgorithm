N = int(input())
arr = list(map(int, input().split()))
arr.sort()


def lower_bound(key):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = int((left + right) / 2)
        print(mid)
        if key > arr[mid]:
            left = mid + 1
        elif key <= arr[mid]:
            right = mid

    return mid


def upper_bound(key):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = int((left + right) / 2)
        if key >= arr[mid]:
            left = mid + 1
        elif key < arr[mid]:
            right = mid

    return mid


M = int(input())
temp = list(map(int, input().split()))

print(sorted(arr))
for value in temp:
    print("upper: ", upper_bound(value), "lower: ", lower_bound(value))
for value in temp:
    print(upper_bound(value) - lower_bound(value), end=" ")
