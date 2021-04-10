S = input()

S_upper = S.upper()
S_lower = S.lower()
ans = ""

for i in range(len(S)):
    if S[i] == S_upper[i]:
        ans += S[i].lower()
    elif S[i] == S_lower[i]:
        ans += S[i].upper()

print(ans)