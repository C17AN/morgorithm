from collections import deque
T = int(input())


def checkQueue(docList, N, M):
    markList = deque()
    cnt = 0
    for i in range(N):
        if i == M:
            markList.append("O")
            continue
        markList.append("X")

    while 1:
        top = docList[0]

        if max(docList) != top:
            popped = docList.popleft()
            docList.append(popped)

            poppedMark = markList.popleft()
            markList.append(poppedMark)
        else:
            cnt += 1
            docList.popleft()
            markList.popleft()

        if "O" not in markList:
            return cnt

    return -1


for i in range(T):
    N, M = map(int, input().split())
    docList = deque(list((map(int, input().split()))))
    print(checkQueue(docList, N, M))
