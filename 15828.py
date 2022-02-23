from collections import deque
s = deque()
threshold = int(input())

while True:
    number = int(input())
    if number == -1:
        if not s:
            print("empty")
            break
        else:
            print(*s)
            break

    if number != 0:
        if len(s) >= threshold:
            continue
        s.append(number)
    else:
        s.popleft()
