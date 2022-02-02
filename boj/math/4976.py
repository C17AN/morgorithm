case = 1

while True:
    ans = 0
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    else:
        ans = V // P * L + min(V % P, L)
    print("Case {}: {}".format(case, ans))
    case += 1
