N = int(input())
stack = []

for _ in range(N):
    temp = int(input())
    if temp == 0:
        stack.pop()
    else:
        stack.append(temp)

print(sum(stack))
