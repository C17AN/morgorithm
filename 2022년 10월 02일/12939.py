def solution(s):
    numList = list(map(lambda el: int(el), s.split(" ")))
    return "{} {}".format(min(numList), max(numList))


print(solution("1 2 3 4"))
