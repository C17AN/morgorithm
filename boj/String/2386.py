while 1:
    alpha = input().split()

    if alpha[0] == '#':
        break

    count = 0
    for i in range(1, len(alpha)):
        alpha[i] = alpha[i].lower()

    for i in alpha[1:]:
        count += i.count(alpha[0])

    print(alpha[0], count)
