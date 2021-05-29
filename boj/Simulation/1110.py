N = int(input())
next_number = N
cnt = 0

while 1:
    prev_number = next_number
    new_number = prev_number // 10 + prev_number % 10
    next_number = prev_number % 10 * 10 + new_number % 10
    cnt += 1
    if next_number == N:
        break

print(cnt)