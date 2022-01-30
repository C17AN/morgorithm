import sys
from heapq import *

input = sys.stdin.readline

N = int(input())
board = []

for i in range(N):
    temp = list(map(int, input().split()))
    for el in temp:
        heappush(board, el)
        if len(board) > N:
            heappop(board)

print(board[0])
