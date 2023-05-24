from collections import deque


def solution(n, computers):
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        y, x = q.popleft()
        for computer in range(computers[y]):
            for node in range(computer):
                if computers[computer][node]:
                    q.append(computer, node)
                    visited[computer][node] = True


solution(3,
         [[1, 1, 0]
          [1, 1, 0]
             [0, 0, 1]])

[[1, 1, 0]
 [1, 1, 0]
 [0, 0, 1]]
