T = int(input())
S = input()
number_stack = []
operator_stack = []
numbers = []

for i in range(T):
    numbers.append(int(input()))

for i in S:
    if 'A' <= i <= 'Z':
        number_stack.append(numbers[ord(i) - 65])
    else:
        a = number_stack.pop()
        b = number_stack.pop()
        if i == "+":
            number_stack.append(a + b)
        if i == "-":
            number_stack.append(b - a)
        if i == "*":
            number_stack.append(a * b)
        if i == "/":
            number_stack.append(b / a)

print(format(*number_stack, ".2f"))
