arr = []

for i in range(3):
    arr.append(int(input()))

a, b, c = arr
if a == b and b == c and a == c:
    print('Equilateral')
elif sum(arr) == 180 and (a == b or a == c or b == c):
    print('Isosceles')
elif sum(arr) == 180:
    print('Scalene')
else:
    print("Error")
