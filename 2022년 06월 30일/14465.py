N, K, B = map(int, input().split())
arr = []
accumulateSum = [1] * N
ans = 0

for _ in range(B):
    accumulateSum[int(input()) - 1] = 0

for i in range(1, N):
    accumulateSum[i] += accumulateSum[i - 1]


for i in range(K - 1, N):
    ans = max(ans, accumulateSum[i] - accumulateSum[i - K])

print(K - ans)
