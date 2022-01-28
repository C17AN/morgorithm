N = int(input())
cnt = 0

for _ in range(N):
    s = []
    word = input()
    for char in word:
        if s:
            if s[-1] == char:
                s.pop()
            else:
                s.append(char)
        else:
            s.append(char)

    if len(s) == 0:
        cnt += 1

print(cnt)
