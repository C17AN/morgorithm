n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
left = 0
right = n - 1
count = 0

while left < right:
    temp = arr[left] + arr[right]
    if temp < x:
        left += 1
    elif temp > x:
        right -= 1
    else:
        count += 1
        right -= 1

print(count)
