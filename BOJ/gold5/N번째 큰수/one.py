import sys
import heapq

sys.stdin = open("input.txt")

N = int(input())
data_list = [list(map(int, input().split())) for i in range(N)]

window = []

for i in range(N):
    heapq.heappush(window, [-data_list[-1][i], i, N - 1])

for _ in range(N):
    val, col, row = heapq.heappop(window)
    heapq.heappush(window, [-data_list[row - 1][col], col, row - 1])
print(-val)