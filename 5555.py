targetString = input()
N = int(input())
rings = []
ringCount = 0
for _ in range(N):
    tempString = input()
    rings.append(tempString * 2)

for ring in rings:
    if targetString in ring:
        ringCount += 1

print(ringCount)
