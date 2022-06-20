X = int(input())
isDividable = False
if X < 10:
    if X % 3 == 0:
        isDividable = True
    print(0)
    if(isDividable):
        print("YES")
    else:
        print("NO")

else:
    valueList = list(str(X))
    valueSum = 0
    isDividable = False

    for value in valueList:
        valueSum += int(value)
    count = 1

    if valueSum < 10:
        if valueSum % 3 == 0:
            isDividable = True
        print(count)
        if(isDividable):
            print("YES")
        else:
            print("NO")

    while valueSum >= 10:
        valueList = list(str(valueSum))
        valueSum = 0
        for value in valueList:
            valueSum += int(value)
        count += 1
        if valueSum < 10:
            if valueSum % 3 == 0:
                isDividable = True
            print(count)
            if(isDividable):
                print("YES")
            else:
                print("NO")
