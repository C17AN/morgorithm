N = int(input())

palindrome_cnt = 0


def make_bin(N, i):
    res = 0
    temp = 0
    digit = 1
    while N > 0:
        temp = N % i
        res = res + (temp * digit)
        digit *= 10
        N //= i
    return res


def check_palindrome(S):
    isPalindrome = True
    for i in range(len(S)):
        if S[i] != S[len(S) - i - 1]:
            isPalindrome = False

    return isPalindrome


for i in range(2, 11):
    S = str(make_bin(N, i))
    if check_palindrome(S):
        palindrome_cnt += 1
        print(i, S)

if palindrome_cnt == 0:
    print("NIE")
