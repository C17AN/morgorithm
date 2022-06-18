N, M = map(int, input().split())
nameDict = {}
nameList = []

for index in range(N):
    name = input()
    nameDict[name] = True

for index in range(M):
    name = input()
    try:
        if nameDict[name] == True:
            nameList.append(name)
    except:
        continue

print(len(nameList))
for name in sorted(nameList):
    print(name)
