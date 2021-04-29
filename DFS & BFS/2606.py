from collections import deque

N = int(input())
T = int(input())

connection = [0]
infected = [False] * (N + 1)

for _ in range(T):
    connection.append(list(map(int, input().split())))


def BFS():
    s = []
    s.append(1)
    while s:
        next_com = s.pop()
        infected[next_com] = True
        for i in range(1, T + 1):
            if connection[i][0] == next_com and infected[connection[i]
                                                         [1]] == False:
                s.append(connection[i][1])
            if connection[i][1] == next_com and infected[connection[i]
                                                         [0]] == False:
                s.append(connection[i][0])


BFS()
print(infected.count(True) - 1)