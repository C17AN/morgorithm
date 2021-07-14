s = []
cnt = 1
needOperation = 0


while 1:
    string = input()
    if('-' in string):
        break

    for letter in string:
        if letter == "{":
            s.append(letter)
        elif letter == "}":
            if s:
                s.pop()
            else:
                needOperation += 1
                s.append("{")
    # print(s)
    needOperation += len(s) // 2

    print("{}. {}".format(cnt, needOperation))
    cnt += 1
    s = []
    needOperation = 0
