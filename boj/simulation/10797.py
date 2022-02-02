N = int(input())
cars = list(map(int, input().split()))
cnt = 0

for car in cars:
    if N == car:
        cnt += 1

print(cnt)
