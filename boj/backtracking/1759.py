L, C = map(int, input().split())
characters = list(input().split())
characters.sort()
password = []
visited = [0] * C


def backtrack(depth, start):
    if depth == L:
        consonant = 0
        vowel = 0
        for word in password:
            if word == "a" or word == "e" or word == "i" or word == "o" or word == "u":
                vowel += 1
            else:
                consonant += 1
        if consonant >= 2 and vowel >= 1:
            for word in password:
                print(word, end="")
            print()
        return

    for i in range(start, C):
        if visited[i] == False:
            visited[i] = True
            password.append(characters[i])
            backtrack(depth + 1, i + 1)
            visited[i] = False
            password.pop()


backtrack(0, 0)
