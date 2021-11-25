import sys
import heapq

data_list = [4, 6, 12, 7, 9]
heapq.heapify(data_list)
print(heapq.heappop(data_list))


# sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
littles_heap = []
larges_heap = []

for _ in range(N):
    num = int(input())
    if len(littles_heap) == len(larges_heap):
        pass
    print(len(heap))
