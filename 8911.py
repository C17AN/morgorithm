T = int(input())
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def checkPosition(y, x, maxY, maxX, minY, minX):
    if y > maxY:
        maxY = y
    elif y < minY:
        minY = y
    if x > maxX:
        maxX = x
    elif x < minX:
        minX = x
    return maxY, maxX, minY, minX


for i in range(T):
    y, x = 0, 0
    maxY, maxX, minY, minX = 0, 0, 0, 0
    headingIndex = 0

    commands = input()
    for command in commands:

        if command == "F":
            # print("y: ", y, " x: ", x)
            y += dy[headingIndex]
            x += dx[headingIndex]
            maxY, maxX, minY, minX = checkPosition(
                y, x, maxY, maxX, minY, minX)

        elif command == "B":
            # print("y: ", y, " x: ", x)
            y -= dy[headingIndex]
            x -= dx[headingIndex]
            maxY, maxX, minY, minX = checkPosition(
                y, x, maxY, maxX, minY, minX)

        elif command == "L":
            if headingIndex > 0:
                headingIndex -= 1
            else:
                headingIndex = 3

        elif command == "R":
            if headingIndex < 3:
                headingIndex += 1
            else:
                headingIndex = 0

    # print(maxY, minY, maxX, minX)
    print(abs(maxY - minY) * abs(maxX - minX))
