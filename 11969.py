import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
acc = [(0, 0, 0)]

for i in range(1, N + 1):
    cowId = int(input())
    prevA, prevB, prevC = acc[i - 1]
    if cowId == 1:
        acc.append((prevA + 1, prevB, prevC))
    elif cowId == 2:
        acc.append((prevA, prevB + 1, prevC))
    elif cowId == 3:
        acc.append((prevA, prevB, prevC + 1))


# print(acc)

for _ in range(Q):
    a, b = map(int, input().split())
    prevA, prevB, prevC = acc[a - 1]
    nextA, nextB, nextC = acc[b]
    print(nextA - prevA, nextB - prevB, nextC - prevC)
