while 1:
    N = input()
    alphabets = [False] * 26
    ans = 0

    if N == '#':
        break

    N = N.lower()

    for i in N:
        if i.isalpha():
            alphabets[ord(i) - 97] = True

    for alpha in alphabets:
        if alpha == True:
            ans += 1

    print(ans)