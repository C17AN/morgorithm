N, K = map(int, input().split())
arr = list(map(int, input().split()))

leftPointer = 0
rightPointer = 1
temperatureSum = arr[0]
prevSum =0
maxTemperature = 0

while leftPointer < N:
  tempSum = sum(arr[leftPointer:rightPointer])
  print(leftPointer, rightPointer, prevSum, tempSum)

  if tempSum < prevSum:
    rightPointer += 1
    prevSum = tempSum
  elif tempSum >= prevSum:
    leftPointer += 1
  else:
    rightPointer += 1

print(prevSum)