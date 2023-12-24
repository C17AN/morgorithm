while True:
    stack = []
    unharmony = False
    S = input()
    if(S == '.'): break

    if('[' not in S and '(' not in S and ')' not in S and ']' not in S):
        print("yes")
        continue

    for char in S:
        if char == '[' or char == '(':
            stack.append(char)
        elif char == ']':
            if('[' not in stack):
                unharmony = True                
                continue
            
            if(stack and stack[-1] == '['):
                stack.pop()

        elif char == ')':
            if('(' not in stack):
                unharmony = True                
                continue
            
            if(stack and stack[-1] == '('):
                stack.pop()                


    if('[' in stack or '(' in stack or ']' in stack or ')' in stack or unharmony):
        print('no')
    else:
        print('yes')
    
                    
        

