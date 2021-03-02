import sys
sys.stdin = open('input.txt')
from collections import deque

input = sys.stdin.readline

N,M = list(map(int,input().split()))
maps = [list(input()) for _ in range(N)]
di = [0,0,-1,1]
dj = [1,-1,0,0]
init_ans = 1000000

def bfs():
    q = deque()
    q.append((0,0,0))
    visited = [[[init_ans]*2 for j in range(M)] for i in range(N)]
    visited[0][0][0] = 1
    while q:
        row, col, wall_break = q.popleft()
        for i in range(4):
            new_row = row+di[i]
            new_col = col+dj[i]
            cnt = visited[row][col][wall_break]
            if -1<new_row<N and -1<new_col<M:
                if maps[new_row][new_col] == '0' and visited[new_row][new_col][wall_break] == init_ans:
                    visited[new_row][new_col][wall_break] = cnt + 1
                    q.append((new_row,new_col, wall_break))
                elif maps[new_row][new_col] == '1' and wall_break == 0 and visited[new_row][new_col][wall_break+1] == init_ans:
                    visited[new_row][new_col][wall_break+1] = cnt + 1
                    q.append((new_row,new_col,wall_break+1))
    return min(visited[N-1][M-1])
                

ret = bfs()
print(-1) if ret==init_ans else print(ret)