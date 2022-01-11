from collections import deque

N, M = map(int, input().split())
cost = 0

rail = deque()
containerList = []

def checkCurrentPriority():
  global M
  isLeft = False
  for item in rail:
    P, W = item
    if P == M:
      isLeft = True
      return isLeft
  M -= 1
  return isLeft

def checkContainerStatus(newContainer):
  global cost
  newP, newW = newContainer
  restArea = deque()
  for container in containerList:
    P, W = container
    cost += W
    if W > newW:
      containerList.append((P, W))
      return

# 초기 레일 적재
for i in range(N):
  P, W = map(int, input().split())
  rail.append((P, W))

# 레일 정렬 작업
while rail:
  P, W = rail.popleft()
  checkCurrentPriority()
  # 우선순위 낮으면 뒤로
  if P < M:
    cost += W
    rail.append((P, W))
  # 컨테이너 적재작업
  else:
    checkContainerStatus((P, W))

print(cost)

