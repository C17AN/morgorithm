N, M = map(int, input().split())
sum = 0
cards = list(map(int, input().split()))


def getSum():
    global sum
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if cards[i] + cards[j] + cards[k] > sum and cards[i] + cards[
                        j] + cards[k] <= M:
                    sum = cards[i] + cards[j] + cards[k]
    return sum


print(getSum())