T = int(input())

d = [0] * 100001
arr = list(map(int, input().split()))
ans_list = []
temp_list = []

d[0] = arr[0]

for i in range(1, T):
    temp_list.append(arr[0])
    for j in range(i, T):
        d[j] = d[j - 1] + arr[j]
        temp_list.append(d[j])

    ans_list.append(max(temp_list))
    # 초기화
    d = [0] * 100001
    temp_list = []

print(max(ans_list))