N = int(input())

for i in range(N):
  S = input()
  strLen = len(S)
  if strLen % 2 == 0:
    for i in range(strLen):
      if i % 2 == 0:
        print(S[i], end="")
    print()
    for i in range(strLen):
      if i % 2 == 1:
        print(S[i], end="")
    print()
      
  else:
    S = S + S
    strLen = len(S)
    for i in range(strLen):
      if i % 2 == 0:
        print(S[i], end="")
    print()
    for i in range(strLen):
      if i % 2 == 1:
        print(S[i], end="")
    print()
    

# L이 짝수일 경우 : str[0] + str[2] + str[N - 1]...
# L이 홀수일 경우 : str을 한번 이어붙인 후, str[0] + str[2] + str[4] + ...str[2N / 2 - 1]
