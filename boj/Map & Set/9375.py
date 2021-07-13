T = int(input())
for _ in range(T):
    clothingList = []
    countMap = {}
    ans = 1

    N = int(input())
    for i in range(N):
        name, category = input().split()
        clothingList.append([name, category])
    clothingDict = dict(clothingList)

    for i in clothingDict.values():  # 맵 키값 0으로 초기화
        countMap[i] = 1
    for i in clothingDict.values():
        countMap[i] += 1

    for i in countMap.values():
        ans *= i
    print(ans - 1)
