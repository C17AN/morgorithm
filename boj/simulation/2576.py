numbers = []
res = 0
initialValue = 999
minOdd = initialValue

for i in range(7):
    numbers.append(int(input()))

for number in numbers:
    if number % 2 == 1:
        res += number
        if number < minOdd:
            minOdd = number

if minOdd == initialValue:
    print(-1)
else:
    print(res)
    print(minOdd)
