N = int(input())
runnerMap = {}
for _ in range(N):
    name = input()
    try:
        runnerMap[name] += 1
    except:
        runnerMap[name] = 0

for _ in range(N - 1):
    name = input()
    runnerMap[name] -= 1

for item in runnerMap.items():
    name, value = item
    if value == 0:
        print(name)
        break
