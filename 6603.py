from itertools import combinations

while True:
    inputs = list(map(int, input().split()))
    if (inputs == [0]):
        break
    numberList = inputs[1:]
    for p in combinations(numberList, 6):
        for number in p:
            print(number, end=" ")
        print()
    print()
