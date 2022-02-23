import heapq

N, M = map(int, input().split())

studentList = []
problems = list(map(int, input().split()))

for _ in range(M):
    temp = list(input().split())
    student, studentScore = int(temp[0]), temp[1:]
    totalScore = 0
    for index in range(len(studentScore)):
        if studentScore[index] == "O":
            totalScore += problems[index]

    heapq.heappush(studentList, (-totalScore, student))

score, student = heapq.heappop(studentList)
print(student, -score)
