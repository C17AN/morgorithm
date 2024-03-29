def toBinary(number):
    acc = ""
    while number:
        acc += str(number % 2)
        number //= 2
    return acc


def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        answer[1] += s.count('0')
        s = s.replace("0", "")
        s = toBinary(len(s))
        print(s)
    return answer
