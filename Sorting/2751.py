T = int(input())
arr = []

for _ in range(T):
    tmp = int(input())
    arr.append(tmp)

arr.sort()

for i in arr:
    print(i)