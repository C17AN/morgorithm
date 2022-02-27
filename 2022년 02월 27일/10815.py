N = int(input())
cardSet = {}
cardList = list(map(int, input().split()))
for card in cardList:
    try:
        cardSet[card] = True
    except:
        cardSet[card] = True

M = int(input())
hasCardList = list(map(int, input().split()))
for card in hasCardList:
    try:
        if cardSet[card] == True:
            print("1", end=' ')
    except:
        print("0", end=' ')
