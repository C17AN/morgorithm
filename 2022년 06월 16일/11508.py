N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)
for index in range(1, len(arr) + 1):
    if index % 3 == 0:
        arr[index - 1] = 0

# print(arr)
print(sum(arr))
