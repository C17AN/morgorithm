N, M = map(int, input().split())
A = {}
B = {}

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

ACount = len(listA)
BCount = len(listB)

for item in listA:
    A[item] = True

for item in listB:
    B[item] = True

for item in listA:
    try:
        if B[item] == True:
            B[item] = False
            BCount -= 1
    except:
        continue

for item in listB:
    try:
        if A[item] == True:
            A[item] = False
            ACount -= 1
    except:
        continue

print(ACount + BCount)
