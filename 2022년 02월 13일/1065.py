N = int(input())
cnt = 0


def isSequence(N):
    numbers = []
    while N:
        numbers.append(N % 10)
        N //= 10
    if len(numbers) >= 2:
        gap = numbers[0] - numbers[1]
        for i in range(len(numbers) - 1):
            if numbers[i] - numbers[i + 1] != gap:
                return False
    else:
        return True
    return True


for i in range(1, N + 1):
    if isSequence(i) == True:
        cnt += 1

print(cnt)
