from collections import deque

N, K = map(int, input().split(" "))
visited = [False] * 100000


def bfs(x):
    count = 0
    isTeleport = False
    q = deque()
    q.append(x)
    while q:
        x = q.popleft()
        if (x == K):
            return count
        for i in range(3):
            if (i == 0):
                nx = x + 1
                q.append(nx)
            elif (i == 1):
                nx = x - 1
                q.append(nx)
            elif (i == 2):
                nx = 2 * x
                q.append(nx)
                isTeleport = True
            count += 1
            if isTeleport == True:
                count -= 1
                isTeleport = False


print(bfs(N))
