from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
incoming = [0] * (N + 1)
times = [0] * (N + 1)
timeSum = 0
timeDP = [0] * (N + 1)

for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    time, n, dists = temp[0], temp[1], temp[2:]
    times[i] = time
    for node in dists:
        graph[node].append(i)
        incoming[i] += 1

q = deque()
for i in range(1, N + 1):
    if incoming[i] == 0:
        q.append(i)
        timeDP[i] = times[i]


# print(graph)
# print(incoming)
# timeSum = times[1]

while q:
    dist = q.popleft()
    for node in graph[dist]:
        # print(node)
        incoming[node] -= 1
        timeDP[node] = max(timeDP[node], timeDP[dist] + times[node])
        # print(timeDP)
        if incoming[node] == 0:
            q.append(node)
            # timeSum += times[node]
            # print(timeSum)


print(max(timeDP))
