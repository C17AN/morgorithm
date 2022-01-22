N, K = map(int, input().split())
coinList = []
cnt = 0

for i in range(N):
    coinList.append(int(input()))

for i in range(len(coinList) - 1, -1, -1):
    cnt += (K // coinList[i])
    K %= coinList[i]
    if K == 0:
        break

print(cnt)
