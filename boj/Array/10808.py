import sys

input = sys.stdin.readline
alphabet = [0] * 26
word = input().rstrip()

for character in word:
    alphabet[ord(character) - ord('a')] += 1

print(*alphabet)
