import time
N = int(input())
count = 0


def fib(N):
    global count
    count += 1
    print("호출 횟수: ", count)
    if N == 0 or N == 1:
        return N
    return fib(N - 1) + fib(N - 2)


start_time = time.time()
print(fib(N))
print("--- 입력값: {}, 실행시간: {} seconds ---".format(N, time.time() - start_time))