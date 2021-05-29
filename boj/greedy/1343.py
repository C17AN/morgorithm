S = input()
cnt = 0

for i in range(len(S)):
    cnt += 1
    newStr = ""
    if S[i] == ".":
        if cnt == 4:
            
