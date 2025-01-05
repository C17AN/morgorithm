def solution(diffs, times, limit):
    def can_complete_with_level(level):
        cur_limit = limit
        time_prev = 0
        
        for index, diff in enumerate(diffs):
            if diff <= level:
                cur_limit -= times[index]
            else:
                cur_limit -= (times[index] * (diff - level + 1)) + time_prev * (diff - level)
            
            if cur_limit < 0:
                return False
            
            time_prev = times[index]
        return True

    # 이진 탐색으로 최적의 level 찾기
    left, right = min(diffs), max(diffs)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_complete_with_level(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer
