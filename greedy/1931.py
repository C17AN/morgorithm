T = int(input())
roomList = []
endTime = 0
cnt = 0

for i in range(T):
    roomList.append(list(map(int, input().split())))

# 두 번째 원소 기준으로
roomList = sorted(roomList, key=lambda x: (x[1], x[0]))
endTime = roomList[0][1]
cnt += 1

for room in roomList[1:]:
    # print(room, endTime, cnt)
    if room[0] < endTime:
        continue

    else:
        cnt += 1
        endTime = room[1]


print(cnt)
