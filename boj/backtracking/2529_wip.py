N = int(input())
operators = input().split(' ')

numbersUsed = [False] * 10
maxNumber = 0
minNumber = 0
number = []

def backtrack(depth):
  if depth == N:
    print(number)
    return
  for i in range(10):
    if not number:
      number.append(i)
      numbersUsed[i] = True
      continue    
    
    if numbersUsed[i] == True:
      continue

    if operators[depth] == '<':
      if number[depth] < i:
        number.append(i)
        numbersUsed[i] = True
        backtrack(depth + 1)
        number.pop()
        numbersUsed[i] = False

    elif operators[depth] == '>':
      if number[depth] > i:
        number.append(i)
        numbersUsed[i] = True
        backtrack(depth + 1)
        number.pop()
        numbersUsed[i] = False

backtrack(0)