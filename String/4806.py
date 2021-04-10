while 1:
    try:
        s = input()
        for i in range(len(s)):
            if s[i] == '\n':
                print("found")
    except:
        break
