N = 1000 - int(input())
cnt = 0

while N:
    if N >= 500:
        N -= 500
        cnt += 1
    elif N >= 100:
        N -= 100
        cnt += 1
    elif N >= 50:
        N -= 50
        cnt += 1
    elif N >= 10:
        N -= 10
        cnt += 1
    elif N >= 5:
        N -= 5
        cnt += 1
    elif N >= 1:
        N -= 1
        cnt += 1

print(cnt)
