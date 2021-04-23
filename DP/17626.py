import math

T = int(input())
temp = T
sqr_t = int(math.sqrt(T))
temp_sqr_t = sqr_t
d = []
cnt = 0

for i in range(sqr_t + 1):
    d.append(i**2)

while temp:
    for i in range(temp_sqr_t):
        if temp >= d[temp_sqr_t - i]:
            temp -= d[temp_sqr_t - i]
            cnt += 1
        if cnt > 4:
            temp = T
            cnt = 0
            sqr_t = temp_sqr_t

print(cnt)