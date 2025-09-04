

def solution(elements):
    s = set()
    for i in range(len(elements)):
        for index, element in enumerate(elements):
            if index + i < len(elements):
                s.add(sum(elements[index:index + i + 1]))
            else:
                 s.add(sum(elements[index:index + i + 1]) + sum(elements[0:index + i - len(elements)]))
    
    answer = len(s)
    return answer