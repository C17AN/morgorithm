from collections import deque

N, M, T = map(int, input().split())

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

castle = []

def gram(start_y, start_x):
    q = deque()
    q.append((start_y, start_x, 0))
    visited = [[False] * M for _ in range(N)]
    visited[start_y][start_x] = True
    
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if ny == N - 1 and nx == M - 1:
                return cnt + 1
            if 0 <= ny < N and 0 <= nx < M:
                if castle[ny][nx] == 2 and visited[ny][nx] == False:
                    return cnt + 1 + (N - ny - 1) + (M - nx - 1)
                elif castle[ny][nx] == 0 and visited[ny][nx] == False:
                    q.append((ny, nx, cnt + 1))
                    visited[ny][nx] = True
    return float('inf')                    
                
                
                
def princess(start_y, start_x):
    q = deque()
    q.append((start_y, start_x, 0))
    visited = [[False] * M for _ in range(N)]
    visited[start_y][start_x] = True
    
    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if ny == N - 1 and nx == M - 1:
                return cnt + 1
            if 0 <= ny < N and 0 <= nx < M:
                if castle[ny][nx] == 0 and visited[ny][nx] == False:
                    q.append((ny, nx, cnt + 1))
                    visited[ny][nx] = True
    return float('inf')
            


for row in range(N):
    castle.append(list(map(int, input().split(' '))))
    
    
    
gramDist = gram(0, 0)
princessDist = princess(0, 0)
        
ans = min(gramDist, princessDist)


if(T < ans):
    print('Fail')
else:
    print(ans)