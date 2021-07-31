import sys
input = sys.stdin.readline

operators = {"/": 2, "*": 2, "+": 1, "-": 1, "(": 0}
stack = []
foluma = input()

for s in foluma:
    if s == "\n":
        continue
    if s.isalpha():
        print(s, end="")
    elif s == "(":
        stack.append(s)
    elif s == ")":
        while True:
            temp = stack.pop()
            if temp == "(":
                break
            print(temp, end="")
    else:
        # 스택의 가장 위에 있는 연산자가 현재 만난 연산자보다 우선순위가 높다면
        # Ex. 스택에는 * 있고 현재 +을 만났다면 스택에 있는걸 먼저 수행함
        # Ex. 스택에는 + 있고 현재 *을 만났다면 그냥 스택에 더하기만 할것 => 이래야 우선순위 높은 순서대로 실행되므로
        while stack and operators[stack[-1]] >= operators[s]:
            print(stack.pop(), end="")
        stack.append(s)

while stack:
    print(stack.pop(), end="")
