N, P = map(int, input().split())
s = [[] for _ in range(7)]
cnt = 0

for i in range(N):
    line, flat = map(int, input().split())
    while True:
        if s[line] and s[line][-1] == flat:
            break
        if not s[line] or s[line][-1] < flat:
            s[line].append(flat)
            cnt += 1
            break
        else:
            while s[line] and s[line][-1] > flat:
                s[line].pop()
                cnt += 1

print(cnt)
