import time
import bisect

# 100만 개의 숫자로 이루어진 정렬된 리스트 생성
data = list(range(1, 1_000_001))

# 찾으려는 값들
search_values = [10, 100_000, 500_000, 900_000, 1_000_000]

# 1. for 루프를 사용한 탐색
start_time = time.time()
for value in search_values:
    found = False
    for num in data:
        if num == value:
            found = True
            break
    if not found:
        print(f"{value} not found")
end_time = time.time()
print(f"For loop search time: {end_time - start_time:.6f} seconds")

# 2. bisect 모듈을 사용한 탐색
start_time = time.time()
for value in search_values:
    index = bisect.bisect_left(data, value)
    if index < len(data) and data[index] == value:
        pass  # Found the value
    else:
        print(f"{value} not found")
end_time = time.time()
print(f"Bisect search time: {end_time - start_time:.6f} seconds")
