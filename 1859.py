T = int(input())

for idx in range(T):
    last = 0
    result = 0

    N = int(input())
    arr = list(map(int, input().split()))
    for index, el in enumerate(reversed(arr)):
        if(index == 0):
            last = el
            continue
        else:
            if(last > el):
                result += last - el
            else:
                last = el
                
    print("#{} : {}".format(idx + 1, result))