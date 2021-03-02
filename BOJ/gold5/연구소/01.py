import sys
from collections import deque
from copy import deepcopy

sys.stdin = open("input.txt")
input = sys.stdin.readline

di = [0,0,1,-1]
dj = [1,-1,0,0]

def solve():
    N,M = list(map(int, input().split()))
    labs = [list(map(int, input().split())) for _ in range(N)]

    virus = deque()
    walls = []

    max_area = 0

    # 벽을 세울 수 있는 좌표 수집
    for i in range(N):
        for j in range(M):
            if labs[i][j]==2:
                virus.append((i,j))
            if labs[i][j]==0:
                walls.append((i,j))
    
    num_of_wall = len(walls)

    # 벽 선택하기
    for f in range(num_of_wall-2):
        for s in range(f+1,num_of_wall-1):
            for t in range(s+1,num_of_wall):
                labs[walls[f][0]][walls[f][1]] = 3
                labs[walls[s][0]][walls[s][1]] = 3
                labs[walls[t][0]][walls[t][1]] = 3
                area = spread(labs, virus)
                labs[walls[f][0]][walls[f][1]] = 0
                labs[walls[s][0]][walls[s][1]] = 0
                labs[walls[t][0]][walls[t][1]] = 0
                if max_area < area:
                    max_area = area
    return max_area

def spread(labs, virus):
    copy_lab = deepcopy(labs)
    copy_virus = deepcopy(virus)
    area = 0
    N = len(labs)
    M = len(labs[0])
    # print(id(copy_lab))
    while copy_virus:
        i,j = copy_virus.popleft()
        for direction in range(4):
            new_i = i + di[direction]
            new_j = j + dj[direction]
            if -1<new_i<N and -1<new_j<M and copy_lab[new_i][new_j]==0:
                copy_lab[new_i][new_j] = 2
                copy_virus.append((new_i,new_j))
    
    for i in range(N):
        for j in range(M):
            if copy_lab[i][j]==0:
                area += 1
    return area


if __name__=='__main__':
    print(solve())