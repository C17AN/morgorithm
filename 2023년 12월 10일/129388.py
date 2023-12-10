import math

def solution(n, s):
    lower, bigger = math.floor(s / 2), math.ceil(s / 2)
    
    return [lower, bigger]

print(solution(3,1))