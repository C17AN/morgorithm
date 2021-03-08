import sys
sys.setrecursionlimit(10**5)

N = int(input())
a, b, c = 0, 1, 1
temp = 0

# memo = [0] * 1000001

# def fib(N):
#     if N == 1 or N == 0:
#         memo[N] = N
#         return memo[N]
#     if memo[N] != 0:
#         return memo[N]
#     else:
#         memo[N] = (fib(N - 1) % 1000000007 + fib(N - 2) % 1000000007)
#         return memo[N]

for i in range(N):
    temp = c
    a = b % 1000000007
    b = temp % 1000000007
    c = a + b

print(a)

#print(fib(N))