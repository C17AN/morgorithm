N, K = map(int, input().split())
a = list(map(int, input().split()))

right = 0
left = 0
numberCount = {}
answer = 0

while right < N:
    if a[right] not in numberCount:
        numberCount[a[right]] = 0
    if a[left] not in numberCount:
        numberCount[a[left]] = 0        

    if numberCount[a[right]] < K:
        numberCount[a[right]] += 1
        right += 1
    
    else:
        numberCount[a[left]] -= 1
        left += 1
    
    answer = max(answer, right - left)

print(answer)
        

    
