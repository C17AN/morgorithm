T = int(input())
time = [0] * 20
price = [0] * 20
table = [0] * 20
for i in range(T):
    t, p = map(int, input().split())
    time[i] = t
    price[i] = p

for i in range(T):
    table[i + time[i]] = max(table[i + time[i]], table[i] + price[i])
    if table[i] == 0:
        print(table)
        table[i] = table[i - time[i]]

print(max(table[0:T + 1]))

# T P  table  R
# 5 50 0
# 4 40 0
# 3 30 0
# 2 20 0
# 1 10 50
# 1 10 60
# 2 20 60
# 3 30 80
# 4 40 80
# 5 50 90