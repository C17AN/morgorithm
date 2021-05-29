N = int(input())

man_list = [[0, 0]] * 50
rank = [1] * N

for i in range(N):
    man_list[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if man_list[i][0] < man_list[j][0] and man_list[i][1] < man_list[j][1]:
            rank[i] += 1

print(*rank)