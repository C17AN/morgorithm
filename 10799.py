laser = list(input())
s = []
cnt = 0
prev = 0

for piece in laser:
    if piece == '(':
        s.append(piece)
        prev = '('
    else:
        s.pop()
        if prev == ')':
            cnt += 1
            prev = ')'
        else:
            cnt += len(s)
            prev = ')'

print(cnt)
