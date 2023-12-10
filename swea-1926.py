import sys

input = sys.stdin.readline

N = input()

for n in range(1, int(N)):
    targetCount = 0
    for char in str(n):
        if char == '3' or char == '6' or char == '9':
            targetCount += 1
    if(targetCount > 0):
        clap = '-' * targetCount
        print(clap, end=' ')
        continue
    print(n, end=" ")