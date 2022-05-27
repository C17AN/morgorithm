import sys
from collections import deque

T = int(input())

for _ in range(T):
    functions = list(input())
    n = int(input())
    rev = 0

    try:
        s = input()[1:-1]
        stack = deque(list(map(int, filter(None, s.split(',')))))
        for function in functions:
            if function == "R":
                rev += 1
            elif function == "D":
                if rev % 2 == 0:
                    stack.popleft()
                else:
                    stack.pop()
        if rev % 2 == 0:
            print(str((list(stack))).replace(" ", ""))
        else:
            arr = (list(stack))
            arr.reverse()
            print(str(arr).replace(" ", ""))
    except:
        print("error")
