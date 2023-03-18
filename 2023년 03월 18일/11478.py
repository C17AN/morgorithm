S = input()

charDict = {}

for (start, startValue) in enumerate(S):
    for (end, endValue) in enumerate(S):
        subString = S[start:end + 1]
        if (subString in charDict or len(subString) == 0):
            continue
        else:
            charDict[subString] = True

print(len(charDict.keys()))
