T = int(input())
stack = []
balance = 0

for i in range(T):
    s = input()
    for i in s:
        stack.append(i)
    for i in stack:
        temp = stack.pop()
        if temp == ")"
