T = int(input())

num_list = list(map(int, input().split()))
d = [0] * 100001
ans = -1001

for i in range(T):
    d[i] = max(num_list[i], d[i - 1] + num_list[i])
    ans = max(d[i], ans)

print(ans)