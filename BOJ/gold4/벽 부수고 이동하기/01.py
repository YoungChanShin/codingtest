import sys
sys.stdin = open('input.txt')
from collections import deque

input = sys.stdin.readline

N,M = list(map(int,input().split()))
maps = [list(input()) for _ in range(N)]
di = [0,0,-1,1]
dj = [1,-1,0,0]

walls = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == '1':
            walls.append((i,j))
def bfs():
    q = deque()
    q.append((0,0))
    visited = [[0]*M for i in range(N)]
    visited[0][0] = 1
    while q:
        row, col = q.popleft()
        for i in range(4):
            new_row = row+di[i]
            new_col = col+dj[i]
            cnt = visited[row][col]
            if -1<new_row<N and -1<new_col<M and visited[new_row][new_col]==0 and maps[new_row][new_col] == '0':
                if new_row == N-1 and new_col == M-1:
                    return cnt+1
                visited[new_row][new_col] = cnt + 1
                q.append((new_row,new_col))
    return -1

answer = 1000000
for i in range(len(walls)):
    row, col = walls[i][0], walls[i][1]
    maps[row][col] = '0'
    ret = bfs()
    if ret>0:
        answer = min(answer, ret)
    maps[row][col] = '1'

if answer == 1000000:
    print(-1)
else:
    print(answer)