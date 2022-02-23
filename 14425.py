N, M = map(int, input().split())
cnt = 0
wordSet = set(input() for _ in range(N))

for _ in range(M):
    word = input()
    if word in wordSet:
        cnt += 1
print(cnt)
