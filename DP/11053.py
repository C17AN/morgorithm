T = int(input())

num_list = list(map(int, input().split()))
d = [1] * 1000

for i in range(T):
    for j in range(i):
        if num_list[i] > num_list[j] and d[i] <= d[j]:
            d[i] = d[j] + 1

print(max(d))