def solution(sequence, k):
    answer = []
    start, end = 0, 0
    current_sum = sequence[0]
    
    while end < len(sequence):
        if current_sum < k:
            end += 1
            current_sum += sequence[end]
            
        elif current_sum > k:
            current_sum -= sequence[start]
            start += 1
            
        else:
            if not answer or (end - start < answer[1] - answer[0]):
                answer = [start, end]
            start += 1
            current_sum -= sequence[start - 1] 
    
    return answer