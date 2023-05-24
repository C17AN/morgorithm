import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    command = input().strip()
    if (" " in command):
        _, value = command.split(" ")
        stack.append(value)

    else:
        if command == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)

        elif command == 'size':
            print(len(stack))

        elif command == 'empty':
            if stack:
                print(0)

            else:
                print(1)

        elif command == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
