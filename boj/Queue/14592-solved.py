from queue import PriorityQueue

N = int(input())
q = PriorityQueue()
for i in range(1, N + 1):
    S, C, L = map(int, input().split())
    q.put((-S, C, L, i))

print(q.get()[3])
