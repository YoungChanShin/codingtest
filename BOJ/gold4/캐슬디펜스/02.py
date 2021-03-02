# 밀어올리기 과정을 제거한 버전
# kill수 측정 방식 간소화
# bfs 코드 반복문 도입

import sys
sys.stdin = open('input.txt')
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
di = [0,-1,0]
dj = [-1,0,1]

N,M,D = list(map(int,input().split()))

castle = [list(map(int,input().split())) for _ in range(N)]

max_kill = 0

def bfs(line, start):
    if new_castle[N-1-line][start]:
        return (N-1-line, start)
    visited = deepcopy(new_castle)
    q = deque()
    q.append((N-1-line,start,1))
    while q:
        i,j,dis = q.popleft()
        if dis<D:
            for direction in range(3):
                new_i = i+di[direction] 
                new_j = j+dj[direction]
                if -1<new_i and -1<new_j<M:
                    if visited[new_i][new_j] == 1:
                        return (new_i,new_j)
                    if visited[new_i][new_j] == 0:
                        q.append((new_i,new_j,dis+1))
    return []

for p1 in range(M-2):
    for p2 in range(p1+1, M-1):
        for p3 in range(p2+1, M):
            kill = 0
            new_castle = deepcopy(castle)

            for r in range(N):
                target = []
                for p in (p1,p2,p3):
                    ret = bfs(r,p)
                    if ret: target.append(ret)
                
                # target 제거하기
                for row,col in target:
                    if new_castle[row][col]:
                        kill += 1
                        new_castle[row][col] = 0

            if max_kill < kill:
                max_kill = kill

print(max_kill)