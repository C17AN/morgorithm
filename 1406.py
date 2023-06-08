from collections import deque

stack = list(input())
N = int(input())
answer = ""

tempInput = deque([])

for _ in range(N):
    command = input()
    if " " in command:
        _, value = command.split(' ')
        stack.append(value)
    else:
        if command == "L":
            if stack:
                value = stack.pop()
                tempInput.appendleft(value)
        if command == "B":
            if stack:
                stack.pop()
        if command == "D":
            if tempInput:
                value = tempInput.popleft()
                stack.append(value)


for value in tempInput:
    stack.append(value)

print(answer.join(stack))
