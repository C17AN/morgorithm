from collections import deque
# import time

N = int(input())
q = deque([i for i in range(1, N + 1)])

# start = time.time()
while len(q) > 1:
    q.popleft()
    temp = q.popleft()
    q.append(temp)

print(q[0])
# print(time.time() - start)
