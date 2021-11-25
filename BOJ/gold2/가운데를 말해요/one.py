import sys
from queue import PriorityQueue

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
que = PriorityQueue()

for _ in range(N):
    num = int(input())
    que.put(num)
    print((que.get()))
