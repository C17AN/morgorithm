from collections import deque

T = int(input())

dy = [ 2, 1, -1, -2, -2, -1, 1, 2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS(N, start, end):
    q = deque()
    srcY, srcX = start
    distY,distX = end
    visited = [[0] * N for _ in range(N)]
    q.append((srcY, srcX, 0))
    visited[srcY][srcX] = 1
    
    while q:
        y, x, cnt = q.popleft()
        
        if y == distY and x == distX:
            return visited[y][x] - 1
            
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx, cnt + 1))
    
            

for _ in range(T):
    I = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    print(BFS(I, start, end))
    
    
[]