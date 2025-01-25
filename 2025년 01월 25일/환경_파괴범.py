import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

first_attack_start, first_attack_end = map(int, input().split())
second_attack_start, second_attack_end = map(int, input().split())

def handle_attack(start, end):
    for row in range(n):
        if start - 1 <= row <= end - 1:
            # 각 열의 진행 정도
            for column in range(m):
                if board[row][column] == 1:
                    board[row][column] = 0
                    break

def check_remaining():
    ans = 0
    for row in range(n):
        for col in range(m):
            if board[row][col] == 1:
                ans += 1
    return ans

handle_attack(first_attack_start, first_attack_end)
handle_attack(second_attack_start, second_attack_end)

answer = check_remaining()
print(answer)