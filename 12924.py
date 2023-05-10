def solution(n):
    answer = 0
    start = 0
    end = 0
    acc = start
    while start <= end:
        if (acc >= n):
            acc -= start
            start += 1

            if (acc == n):
                print("goal!", start, end, acc)
                answer += 1

        if acc < n:
            acc += end
            end += 1

    print(answer)

    return answer


solution(15)
