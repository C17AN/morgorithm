from collections import deque

T = int(input())

student = []
result = []
check = []
used = set()


def checkTeam(start_node):
    q = deque()
    q.append(start_node)
    checked = []
    while q:
        index = q.pop()
        used.add(index)
        checked.append(index)
        if student[index - 1] not in checked and student[index -
                                                         1] not in used:
            q.append(student[index - 1])
        if student[index - 1] == start_node:
            return checked


for _ in range(T):
    n = int(input())
    student = list(map(int, input().split()))
    for i in range(1, n + 1):
        # print(i, result)
        if i in result:
            continue
        temp = checkTeam(i)
        if temp != None:
            result += temp
    # print(used)
    print(n - len(result))
    result = []
    used = set()
