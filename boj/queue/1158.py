from collections import deque

N, K = map(int, input().split())
q = deque([i for i in range(1, N + 1)])
ansList = []
pointer = 0

while q:
    pointer += 1
    temp = q.popleft()
    if pointer == K:
        pointer = 0
        ansList.append(temp)
        continue
    else:
        q.append(temp)

print('<', end="")
for index in range(len(ansList)):
    if(index < len(ansList) - 1):
        print(ansList[index], end=", ")
    else:
        print(ansList[index], end="")
print('>', end="")
