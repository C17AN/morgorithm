words = []
temp_words = []
while 1:
    T = int(input())
    if T == 0:
        break

    for i in range(T):
        words.append(input())

    for i in range(T):
        temp_words.append(words[i].upper())

    temp_words.sort()
    for word in words:
        if word.upper() == temp_words[0]:
            print(word)

    words = []
    temp_words = []