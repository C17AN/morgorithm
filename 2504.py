brackets = input()
stack = []
temp = 1
ans = 0

for index in range(len(brackets)):
    # print(stack, temp, ans)
    if brackets[index] == "(":
        temp *= 2
        stack.append("(")

    elif brackets[index] == "[":
        temp *= 3
        stack.append("[")

    elif brackets[index] == ")":
        if not stack or stack[-1] != '(':
            ans = 0
            break
        if brackets[index - 1] == '(':
            ans += temp
        temp //= 2
        stack.pop()

    elif brackets[index] == "]":
        if not stack or stack[-1] != '[':
            ans = 0
            break
        if brackets[index - 1] == '[':
            ans += temp
        temp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(ans)
