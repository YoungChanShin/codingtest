import sys
import heapq


sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
first = int(input())
littles_heap = [-first]  # 최대힙
larges_heap = []  # 최소힙(default)

print(first)

for _ in range(N - 1):
    num = int(input())
    if num <= -littles_heap[0]:
        heapq.heappush(littles_heap, -num)
    else:
        heapq.heappush(larges_heap, num)

    while len(littles_heap) < len(larges_heap):
        temp = heapq.heappop(larges_heap)
        heapq.heappush(littles_heap, -temp)

    if len(littles_heap) - len(larges_heap) > 1:
        temp = heapq.heappop(littles_heap)
        heapq.heappush(larges_heap, -temp)

    print(-littles_heap[0])