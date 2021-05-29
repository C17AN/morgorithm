from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([False] * (2 * N))


def run():
    step = 0
    while 1:
        step += 1
        # 벨트 한칸 이동
        belt.appendleft(belt.pop())
        robot.appendleft(robot.pop())

        if robot[N - 1] == True:
            robot[N - 1] = False
        print("벨트 한칸 이동 : ", belt, robot, step)

        # 로봇 한칸 이동
        for i in range(1, N):
            if belt[N - i] > 0 and robot[N - i -
                                         1] == True and robot[N - i] == False:
                robot[N - i] = robot[N - i - 1]
                robot[N - i - 1] = False

            if robot[N - 1] == True:
                robot[N - 1] = False

            if robot[N - i] == True:
                belt[N - i] -= 1
                if belt[N - i] < 0:
                    belt[N - i] = 0

        print("로봇 한칸 이동 : ", belt, robot, step)

        # 로봇 올리고
        if robot[0] == False and belt[0] > 0:
            robot[0] = True
            belt[0] -= 1
        print("로봇 올리고 내리고 : ", belt, robot, step)
        print()

        if belt.count(0) >= K:
            return step


run()
print(*belt)