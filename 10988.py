string = input()
stringLength = len(string)
isPalindrome = True

for (index, letter) in enumerate(string):
    if letter != string[stringLength - index - 1]:
        isPalindrome = False
        print(0)
        break

if isPalindrome:
    print(1)
