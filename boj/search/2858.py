R, B = map(int, input().split())
area = R + B

for h in range(3, R * B + 1):
    l = area / h
    if 2 * l + 2 * (h - 2) == R:
        print(int(l), int(h))
        break
