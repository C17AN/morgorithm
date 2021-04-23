import math

N = input()
numbers = [0] * 10

for i in N:
    numbers[int(i)] += 1

avg = math.ceil((numbers[6] + numbers[9]) / 2)
numbers[6], numbers[9] = avg, avg

print(max(numbers))