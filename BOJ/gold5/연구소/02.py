import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('input.txt')

di = [0,0,1,-1]
dj = [1,-1,0,0]

N,M = list(map(int,input().split()))
data_list = [list(map(int,input().split())) for _ in range(N)]

zeros = []
virus = []
for i in range(N):
    for j in range(M):
        if data_list[i][j]==2:
            virus.append((i,j))
        if data_list[i][j]==0:
            zeros.append((i,j))

def count_zeros(data_list):
    cnt = 0
    for i in range(len(data_list)):
        for j in range(len(data_list[0])):
            if data_list[i][j]==0:
                cnt += 1
    return cnt

def spread(data_list, virus):
    maps = deepcopy(data_list)
    waitings = deque()
    for v in virus:
        waitings.append(v)
    while waitings:
        i,j = waitings.popleft()
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]

            if -1<new_i<len(data_list) and -1<new_j<len(data_list[0]) and maps[new_i][new_j]==0:
                waitings.append((new_i,new_j))
                maps[new_i][new_j] = 3
    return count_zeros(maps)

answer = 0
for i in range(len(zeros)-2):
    for j in range(i+1, len(zeros)-1):
        for k in range(j+1, len(zeros)):
            # print(zeros[i],zeros[j], zeros[k])
            data_list[zeros[i][0]][zeros[i][1]] = 3
            data_list[zeros[j][0]][zeros[j][1]] = 3
            data_list[zeros[k][0]][zeros[k][1]] = 3
            answer = max(answer, spread(data_list,virus))

            data_list[zeros[i][0]][zeros[i][1]] = 0
            data_list[zeros[j][0]][zeros[j][1]] = 0
            data_list[zeros[k][0]][zeros[k][1]] = 0
print(answer)
# print(spread(data_list,virus))