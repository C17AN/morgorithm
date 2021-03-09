N = int(input())
s = [0]
d = [0] * 301

for i in range(N):
    s.append(int(input()))

if N == 1:
    d[1] = s[1]
elif N == 2:
    d[1] = s[1]
    d[2] = s[1] + s[2]
else:
    d[1] = s[1]
    d[2] = s[1] + s[2]
    d[3] = max(s[1] + s[3], s[2] + s[3])

for i in range(4, N + 1):
    d[i] = max(d[i - 3] + s[i - 1] + s[i], d[i - 2] + s[i])

print(d[N])
