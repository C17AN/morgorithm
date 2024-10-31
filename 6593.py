from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
dz = [1, 0, -1]

def findStartPoint(building):
    start = ()
    for levelIndex, level in enumerate(building):
        for rowIndex, row in enumerate(level):
            for colIndex, col in enumerate(row):
                if col == 'S':
                    start = (levelIndex, rowIndex, colIndex)

    return start
    
    
def BFS(start, building):
    z, y, x = start
    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    visited[z][y][x] = True
    q = deque()
    q.append((z, y, x, 0))
    
    
    while q:
        z, y, x, cnt = q.popleft()
        
        for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if 0 <= ny < R and 0 <= nx < C and not visited[z][ny][nx]:
                    if building[z][ny][nx] == '.':
                        visited[z][ny][nx] = True
                        q.append((z, ny, nx, cnt + 1))
                        print(z, ny, nx, cnt + 1)
                        
                    elif building[z][ny][nx] == 'E':
                        print(z, ny, nx, cnt + 1)
                        return cnt + 1
        for j in range(3):            
                nz = z + dz[j]
                if 0 <= nz < L and not visited[nz][y][x]:
                    if building[nz][y][x] == '.':
                        visited[nz][y][x] = True
                        q.append((nz, y, x, cnt + 1))
                        print(nz, y, x, cnt + 1)
                        
                    elif building[nz][y][x] == 'E':
                        print(nz, y, x, cnt + 1)
                        return cnt + 1
                
    return -1
                    
while 1:
    L, R, C = map(int, input().split(' '))
    if L == 0 and R == 0 and C == 0:
        break

    ellapsedTime = 0
    building = []    

    for index, _ in enumerate(range(L)):
        floor = []
        for _ in range(R):
            floor.append(list(input()))
        if index != L - 1:
            input()
        building.append(floor)
        
    start = findStartPoint(building)
    res = BFS(start, building)
    
    if res != -1:
        print('Escaped in {} minute(s).'.format(res))
    else:
        print("Trapped!")
    input()
