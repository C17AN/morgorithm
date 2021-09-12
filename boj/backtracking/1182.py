N, S = map(int, input().split())
numberList = list(map(int, input().split()))
count = 0
tempList = []

def backtrack(idx, numberSum):
    global count
    if idx == N:
        return
    tempSum = numberSum + numberList[idx]
    if tempSum == S:
        count += 1
    tempList.append(numberList[idx])
    # print(tempList, tempSum)
    backtrack(idx + 1, tempSum)
    tempList.pop()
    backtrack(idx + 1, numberSum)


backtrack(0, 0)

print(count)