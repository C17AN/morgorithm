T = int(input())

for i in range(T):
    ans = 0
    S = input()

    while S != "6174":
        s_bigger = int(''.join(sorted(S, reverse=True)))
        s_smaller = int(''.join(sorted(S)))
        S = str(s_bigger - s_smaller)

        if len(S) < 4:
            temp = ""
            for i in range(4 - len(S)):
                temp += '0'
            S = temp + S

        ans += 1

    print(ans)