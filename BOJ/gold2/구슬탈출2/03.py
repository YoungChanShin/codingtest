import sys
sys.stdin = open("input.txt")

from collections import deque

q = deque()

input = sys.stdin.readline
N,M = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]

di = [0,0,1,-1]
dj = [1,-1,0,0]

visited = [[[[0]*M for _ in range(N)] for x in range(M)] for y in range(N)]

ri, rj, bi, bj = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            ri, rj = i, j
            board[i][j] = '.'
        if board[i][j] == "B":
            bi, bj = i, j
            board[i][j] = '.'

q.append([ri,rj,bi,bj,0])
visited[ri][rj][bi][bj] = 1

def move(x,y,d):
    cnt = 0
    while board[x+di[d]][y+dj[d]] == '.':
        x += di[d]
        y += dj[d]
        cnt += 1
    return x, y, cnt

def tilt():
    while q:
        ri,rj,bi,bj,cnt = q.popleft()
        if cnt >= 10:
            return -1
        for i in range(4):
            new_ri, new_rj , r_cnt = move(ri, rj, i)
            new_bi, new_bj , b_cnt = move(bi, bj, i)
            if board[new_bi+di[i]][new_bj+dj[i]] == 'O':
                continue
            elif board[new_ri+di[i]][new_rj+dj[i]] == 'O':
                return cnt+1
            elif new_bi == new_ri and new_bj == new_rj:
                if r_cnt<b_cnt:
                    new_bi -= di[i]
                    new_bj -= dj[i]
                else:
                    new_ri -= di[i]
                    new_rj -= dj[i]
            if visited[new_ri][new_rj][new_bi][new_bj] == 0:
                visited[new_ri][new_rj][new_bi][new_bj] = 1
                q.append([new_ri, new_rj, new_bi, new_bj, cnt+1])
    return -1

print(tilt())
            