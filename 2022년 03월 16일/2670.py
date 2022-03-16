N = int(input())
numbers = [0]

for i in range(1, N + 1):
    numbers.append(float(input()))

d = numbers

for i in range(1, N + 1):
    d[i] = max(numbers[i], d[i - 1] * numbers[i])

print("{:.3f}".format(round(max(d), 3)))
