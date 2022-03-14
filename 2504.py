string = input()
stack = []
ans = 0
value = 1
abnormal = False

for char in string:
    if char == ")":
        if "(" in stack:
            value *= 2
        else:
            ans += value
        else:
            abnormal = True
