from collections import deque

N, M = map(int, input().split())
trust = [[] for _ in range(N + 1)]
count = [0] * (N + 1)


def BFS(node):
    q = deque()
    q.append(node)
    infected = [False] * (N + 1)
    infected[node] = True
    while q:
        node = q.popleft()
        for nextNode in trust[node]:
            if infected[nextNode] == True:
                continue
            else:
                q.append(nextNode)
                infected[nextNode] = True

    return infected.count(True)


for i in range(M):
    dist, src = map(int, input().split())
    trust[src].append(dist)

for node in range(1, N + 1):
    count[node] = BFS(node)

for i in range(len(count)):
    if count[i] == max(count):
        print(i, end=" ")

# N, M = map(int, input().split())
# trust = [[] for _ in range(N + 1)]
# count = [-1] * (N + 1)
# infected = [0 for _ in range(N + 1)]
# cnt = 0
# max_cnt = 0
# for i in range(1, M + 1):
#     dist, src = map(int, input().split())
#     trust[src].append(dist)

# def DFS(node_list):
#     global cnt
#     global infected
#     s = []
#     for node in node_list:
#         s.append(node)

#     while s:
#         next_node = s.pop()
#         infected[next_node] = 1
#         cnt += 1
#         if infected[next_node] != 0:
#             if count[next_node] == -1:
#                 DFS(trust[next_node])
#                 infected[next_node] = 1
#         else:
#             return count[next_node]

#     return cnt

# for i in range(1, len(trust)):
#     count[i] = DFS(trust[i])
#     cnt = 0

# for i in range(1, len(count)):
#     if count[i] == max(count):
#         print(i, end=" ")
