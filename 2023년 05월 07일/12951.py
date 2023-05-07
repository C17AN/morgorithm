def solution(s):
    answer = ''
    string = str(s).lower()
    stringList = string.split(" ")

    for index, string in enumerate(stringList):
        if (string != ""):
            print(string, string.replace(string[0], string[0].upper()))
            stringList[index] = string.replace(string[0], string[0].upper())

    # for index, string in enumerate(stringList):
    #     if (string == ""):
    #         stringList.pop(index)

    answer = " ".join(stringList)
    print(answer)
    return answer


solution("3Hello  2wo   rld 4hi  HAHAHAH    why?  hello")
