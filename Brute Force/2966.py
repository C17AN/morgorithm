N = int(input())
ans = input()

a = ['A', 'B', 'C']
b = [
    'B',
    'A',
    'B',
    'C',
]
c = ['C', 'C', 'A', 'A', 'B', 'B']

a_cnt, b_cnt, c_cnt = 0, 0, 0
max_correct = 0

for i in range(len(ans)):
    if ans[i] == a[i % len(a)]:
        a_cnt += 1
    if ans[i] == b[i % len(b)]:
        b_cnt += 1
    if ans[i] == c[i % len(c)]:
        c_cnt += 1

max_correct = max(a_cnt, max(b_cnt, c_cnt))
print(max_correct)
if a_cnt == max_correct:
    print('Adrian')
if b_cnt == max_correct:
    print('Bruno')
if c_cnt == max_correct:
    print("Goran")
