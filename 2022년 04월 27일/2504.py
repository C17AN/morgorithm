brackets = list(input())
usedBrackets = []
prev = None
current = None
res = 0


def calculate():
    global res
    global current
    global prev
    global usedBrackets

    # res = 0

    while brackets:
        # if usedBrackets:
        #     prev = usedBrackets[-1]
        # else:
        #     prev = None
        current = brackets.pop(0)
        print("prev, current: ", prev, current)

        if prev == "(":
            if current == "[" or current == "(":
                usedBrackets.append(current)
                res += 2 * calculate()
                continue

            elif current == ")":
                usedBrackets.pop()
                prev = ")"
                res += 2
                continue

            else:
                usedBrackets.append(current)
                continue

        elif prev == "[":
            if current == "[" or current == "(":
                usedBrackets.append(current)
                res += 3 * calculate()
                continue

            elif current == "]":
                usedBrackets.pop()
                prev = "]"
                res += 3
                continue

            else:
                usedBrackets.append(current)
                continue

        elif prev == "]":
            if current == "]" or current == ")":
                usedBrackets.pop()
                return res
            elif current == "[":
                res += 3
                usedBrackets.append(current)
                continue
            elif current == "(":
                res += 2
                usedBrackets.append(current)
                continue

        elif prev == ")":
            if current == "]" or current == ")":
                usedBrackets.pop()
                return res
            elif current == "[" or current == "(":
                usedBrackets.append(current)
                continue
        else:
            prev = current
            usedBrackets.append(current)
    print("res: ", res)
    return res


ans = calculate()
print(usedBrackets)
if usedBrackets:
    print(0)
else:
    print(ans)
