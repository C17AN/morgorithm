N = int(input())

s = [False, False, False]

for i in range(N):
    a, b = map(int, input().split())
    if a == 1 and b == 3 or a == 3 and b == 1:
        s[0] = True
    elif a == 1 and b == 4 or a == 4 and b == 1:
        s[1] = True
    elif a == 3 and b == 4 or a == 4 and b == 3:
        s[2] = True
    else:
        s.append(False)

if s[0] and s[1] and s[-1]:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print('Woof-meow-tweet-squeek')
