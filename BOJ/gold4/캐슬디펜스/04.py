# bfs 대신 인덱스로 접근

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

def bfs(line, player):
    if new_castle[N-1-line][player]:
        return (N-1-line, player)    
    minD = D+1
    reti, retj = -1,-1
    arrow_line = N-line
    for i in range(arrow_line):
        for j in range(M):
            distance = abs(i-arrow_line)+abs(j-player)
            # print(distance)
            if new_castle[i][j]>0 and distance<=minD:
                if distance<minD:
                    reti, retj = i,j
                    minD = distance
                elif distance == minD and j<retj:
                    reti, retj = i,j
    if reti+retj>=0:
        return reti, retj
    else:
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