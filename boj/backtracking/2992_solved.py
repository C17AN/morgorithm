X = input()

number = ""
minNumber = "999999"
digit = len(X)
used = [False] * digit

def backtrack(depth):
  global number
  global minNumber

  if depth == digit:
    if X < number < minNumber:
      minNumber = number
    return

  for i in range(digit):
    if used[i] == True:
      continue
    used[i] = True
    number += X[i]
    backtrack(depth + 1)
    used[i] = False
    number = number[:-1]


backtrack(0)

if minNumber == '999999':
  minNumber = 0
print(minNumber)