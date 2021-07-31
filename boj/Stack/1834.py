import sys
from collections import deque
input = sys.stdin.readline

stack = deque()
ansList = deque()
valueList = deque()

N = int(input())

for _ in range(N):
    stack.append(int(input()))

for value in range(1, N + 1):
    valueList.append(value)
    ansList.append('+')
    try:
        while stack and (stack[0] == valueList[-1]):
            stack.popleft()
            valueList.pop()
            ansList.append('-')
    except:
        continue

if stack:
    print('NO')
else:
    for ans in ansList:
        print(ans)
