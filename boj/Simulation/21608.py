N = int(input())
info = [[0] * 4 for i in range(N * N)]
classroom = [[0] * N for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def find_favorite(student, info):
    global classroom
    # (0, 0) 부터 탐색
    best = (0, 0)
    found = 0
    empty = 0
    max_empty = 0
    max_found = 0

    # 실제 이동 (1, 1)부터 (N, N)까지
    for row in range(N):
        for col in range(N):
            if classroom[row][col] != 0:
                continue
            # 사방을 확인
            for i in range(4):
                # 좋아하는 학생을 찾는다
                for j in range(4):
                    if 0 <= row + dy[i] < N and 0 <= col + dx[i] < N:
                        if classroom[row + dy[i]][col +
                                                  dx[i]] == info[student -
                                                                 1][j]:
                            found += 1
                        elif classroom[row + dy[i]][col + dx[i]] == 0:
                            empty += 1

            # 경우 1. 가장 많이 찾은 경우를 저장
            if found > max_found:
                max_found = found
                best = (row, col)
                found = 0

            # 경우 2
            elif found == max_found:
                if max_empty >= empty:
                    best = (row, col)
                    empty = 0
                # 경우 3
                elif max_empty == empty:
                    # 이거 수정
                    best = (row, col)
                    empty = 0

            # else empty >

    classroom[best[0]][best[1]] = student


for i in range(N * N):
    temp = list(map(int, input().split()))
    info[temp[0] - 1] = temp[1:5]

for i in range(1, N * N + 1):
    find_favorite(i, info)
    print(classroom)