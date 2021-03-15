import sys
sys.stdin = open('input.txt')

N = int(input())
house = [input().split() for _ in range(N)]
dp = [[[0,0,0] for i in range(N)] for j in range(N)]

dv = [[[0,0],[1,1]],[[0,1],[1,1]]]
dh = [[[1,1],[0,0]],[[1,1],[0,1]]]
dd = [[[1,0],[1,1]],[[1,1],[1,0]],[[1,1],[1,1]]]

dv = ((0, 0, 1, 1),(0, 1, 1, 1)
dh = ((1,1,0,0),(1,1,0,1))
dd = ((1,0,1,1),(1,1,1,0),(1,1,1,1))

pipe = (0,0,0,1)