import sys
input = sys.stdin.readline

w, n = map(int, input().split())
answer = 0

jewel_info = []

for jewel in range(n):
    weight, price_per_weight = map(int, input().split())
    jewel_info.append([weight, price_per_weight])

jewel_info.sort(key=lambda x: x[1], reverse=True)

for jewel in jewel_info:
    if w >= jewel[0]:
        w -= jewel[0]
        answer += jewel[0] * jewel[1]
    else:
        answer += w * jewel[1]
        break

print(answer)