N, M = map(int, input().split())
arr = []

maxValue = 0

def getDigit(N):
  digit = 0
  while N:
    N //= 10
    digit += 1
  return digit

def makeReverse(N, digit):
  reversed = 0
  for i in range(digit):
    reversed *= 10
    reversed += (N % 10)
    N //= 10

  return reversed

for i in range(1, M + 1):
  digit = getDigit(N * i)
  reversed =  makeReverse((N * i), digit)
  if maxValue < reversed:
    maxValue = reversed

print(maxValue)