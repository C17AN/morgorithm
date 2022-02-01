S = input()
counts = {'1': 0, '0': 0}
changed = False
prev = ''

for char in S:
    if char != prev:
        counts[char] += 1
        prev = char

print(min(counts.values()))
