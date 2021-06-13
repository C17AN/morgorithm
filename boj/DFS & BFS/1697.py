from collections import deque

N, K = map(int, input().split())

board = [0] * 100001
visited = [False] * 100001


def BFS(start):
    q = deque()
    q.append(start)
    cnt = 0
    while q:
        p = q.popleft()
        cnt = p[1]

        if not visited[p[0]]:
            visited[p[0]] = True
            if p[0] == K:
                return p[1]

            cnt += 1

            if p[0] + 1 <= 100000:
                q.append((p[0] + 1, cnt))
            if p[0] - 1 >= 0:
                q.append((p[0] - 1, cnt))
            if p[0] * 2 <= 100000:
                q.append((p[0] * 2, cnt))


print(BFS((N, 0)))
