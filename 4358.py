treeMap = {}

while True:
    try:
        treeName = input()
        try:
            treeMap[treeName] += 1
        except:
            treeMap[treeName] = 1
    except:
        break

length = 0
sortedMap = sorted(treeMap.items())

for item in sortedMap:
    _, value = item
    length += value

for item in sortedMap:
    key, value = item
    print(key, "{:.4f}".format(round(value / length * 100, 4)))
# print(len(treeMap))
