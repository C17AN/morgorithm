ratioSum = 0
scoreList = []
scoreSum = 0

while True:
    try:
        subjectName, ratio, score = input().split()
        if score == "A+":
            score = 4.5
        elif score == "A0":
            score = 4.0
        elif score == "B+":
            score = 3.5
        elif score == "B0":
            score = 3.0
        elif score == "C+":
            score = 2.5
        elif score == "C0":
            score = 2.0
        elif score == "D+":
            score = 1.5
        elif score == "D0":
            score = 1.0
        elif score == "F":
            score = 0
        elif score == "P":
            continue
        ratioSum += int(float(ratio))
        scoreList.append((float(ratio), score))
    except:
        break

for ratio, score in scoreList:
    scoreSum += ratio * score / ratioSum

print(scoreSum)
