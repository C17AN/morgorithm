N, X = map(int,input().split())
board = list(map(int, input().split()))

left = 0
right = 0
answer = 0
initial = 0
accSum = 0
answer2 = 0

for index in range(X):
    initial += board[index]

accSum = initial

for value in range(N - X):
    accSum = accSum - board[value] + board[value + X]
    answer = max(answer, accSum)

accSum = initial
if accSum == answer:
    answer2 += 1

for value in range(N - X):
    accSum = accSum - board[value] + board[value + X]
    if accSum == answer:
        answer2 += 1

if answer == 0:
    print("SAD")
else:
    print(answer)
    print(answer2)