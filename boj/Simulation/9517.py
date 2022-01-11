K = int(input())
N = int(input())

elapsedTime = 0
endTime = 210
currentPerson = K
deadPerson = 0

for i in range(N):
    time, answer = input().split()
    time = int(time)
    if elapsedTime >= endTime and not deadPerson:
      deadPerson = currentPerson
    if answer == 'T':
      if currentPerson == 8:
        currentPerson = 1
      else:
        currentPerson += 1
      elapsedTime += time
    else:
      elapsedTime += time
 

print(deadPerson)