R, C = map(int, input().split())

image = []
filtered = []
cnt = 0


def findMid(R, C):
    global image
    pixels = []
    for row in range(3):
        for col in range(3):
            pixels.append(image[row + R][col + C])
    pixels.sort()
    return pixels[4]


for row in range(R):
    image.append(list(map(int, input().split())))

for row in range(R - 2):
    for col in range(C - 2):
        filtered.append(findMid(row, col))

T = int(input())
for i in filtered:
    if i >= T:
        cnt += 1

print(cnt)