N = int(input())
meetings = []
count = 0

for i in range(N):
    meetings.append(list(map(int, input().split())))


def findMin(start_time):
    end_time = 999
    # 제일 일찍 끝나는거 찾기
    for i in range(N):
        if meetings[i][0] >= start_time:
            if end_time > meetings[i][1]:
                end_time = meetings[i][1]

    return end_time


def findStart():
    start_time = meetings[0][0]
    cnt = 0
    for i in range(N):
        # print(meetings[i][0], start_time)
        if meetings[i][0] < start_time:
            continue
        elif meetings[i][0] >= start_time:
            start_time = findMin(meetings[i][0])
            cnt += 1

    return cnt


print(findStart())
