from collections import deque

N, K = map(int, input().split())
visited = [False] * 400001
answer = 0

q = deque([(N, 0)])

while q:
    flag = False
    value, time = q.popleft()
    visited[value] = True
    if value == K:
        flag = True
        break
    if not visited[value - 1] and value - 1 >= 0:
        q.append((value - 1, time + 1))
        visited[value - 1] = True
    if not visited[value + 1] and value + 1 <= K:
        q.append((value + 1, time + 1))            
        visited[value + 1] = True
    if not visited[2 * value] and 2 * value <= K:
        q.append((2 * value, time + 1))
        visited[value * 2] = True
           
    if flag:
        answer = time
        break


print(time)