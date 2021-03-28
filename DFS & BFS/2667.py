from collections import deque
T = int(input())

board = []
visited = [[False] * T for _ in range(T)]
apartCount = 0
countList = []

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def BFS(start_node):
    s = deque()
    s.append(start_node)
    count = 1
    while len(s) != 0:
        node = s.popleft()
        visited[int(node[0])][int(node[1])] = True

        for i in range(4):
            nextY = int(node[0]) + dy[i]
            nextX = int(node[1]) + dx[i]
            if nextY >= T or nextY < 0 or nextX >= T or nextX < 0 or visited[
                    nextY][nextX] == True or board[nextY][nextX] == '0':
                continue
            else:
                count += 1
                visited[nextY][nextX] = True
                s.append([nextY, nextX])

    return count


for i in range(T):
    board.append(list(input()))

for i in range(T):
    for j in range(T):
        if board[i][j] == '1' and visited[i][j] == False:
            apartCount += 1
            countList.append(BFS([i, j]))

print(apartCount)
countList.sort()
for i in range(len(countList)):
    print(countList[i])