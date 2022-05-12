N = int(input())
for i in range(N):
    s = []
    brackets = list(input())
    for bracket in brackets:
        try:
            if s[-1] == "(" and bracket == ")":
                s.pop()
            else:
                s.append(bracket)
        except:
            s.append(bracket)
    if s:
        print("NO")
    else:
        print("YES")
