while 1:
    submit_state = list(map(int, input().split()))
    if submit_state[0] == 0:
        break
    else:
        ans_set = set()
        ans_list = []
        for i in submit_state[1:]:
            ans_set.add(i)
        print(*ans_set, end='')
        print(" $")