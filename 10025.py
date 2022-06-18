N, K = map(int, input().split())
iceList = []
bucketPositionList = [0] * 1000001

for _ in range(N):
    ice, bucketPosition = map(int, input().split())
    bucketPositionList[bucketPosition] = ice


start = 0
end = K
maxIceValueSum = 0

K = 2 * K + 1
iceValueSum = 0
for i in range(1000001):
    if i >= K:
        iceValueSum -= bucketPositionList[i - K]
    iceValueSum += bucketPositionList[i]
    maxIceValueSum = max(maxIceValueSum, iceValueSum)

print(maxIceValueSum)
