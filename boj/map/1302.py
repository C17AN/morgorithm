N = int(input())
arr = [[] for _ in range(1000)]

books = {}
bookMap = {}

for i in range(N):
    temp = input()
    if temp in books.keys():
        books[temp] += 1
    else:
        books[temp] = 1

for book in books.items():
    name, count = book
    arr[count].append(name)

for i in range(999, 0, -1):
    if arr[i]:
        print(sorted(arr[i])[0])
        break
