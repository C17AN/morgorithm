T = int(input())
endString = "what does the fox say?"


for i in range(T):
    wordList = list(input().split(' '))
    while True:
        string = input()
        if string == endString:
            break
        else:
            parsedString = string.split(' ')
            animal, barking = parsedString[0], parsedString[2]

            for wordIndex in range(len(wordList)):
                if wordList[wordIndex] == barking:
                    wordList[wordIndex] = False

    for word in wordList:
        if word:
            print(word, end=" ")
    print()
