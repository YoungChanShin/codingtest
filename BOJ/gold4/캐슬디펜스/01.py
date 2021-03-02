import sys
sys.stdin = open('input.txt')
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
di = [0,-1,0]
dj = [-1,0,1]

N,M,D = list(map(int,input().split()))

castle = [list(map(int,input().split())) for _ in range(N)]
# castle.append([0]*M)

max_kill = 0

def bfs(start):
    if new_castle[N-1][start]:
        return (N-1, start)
    visited = deepcopy(new_castle)
    q = deque()
    q.append((N-1,start,1))
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

                ret = bfs(p1)
                if ret: target.append(ret)

                ret = bfs(p2)
                if ret: target.append(ret)

                ret = bfs(p3)
                if ret: target.append(ret)
                
                # target 제거하기
                new_target = []
                for i in target:
                    if i not in new_target:
                        new_target.append(i)
                kill += len(new_target)
                for t in new_target:
                    new_castle[t[0]][t[1]] = 0

                # 아래로 밀기
                for ii in range(N-1,r,-1):
                    for j in range(M):
                        new_castle[ii][j] = new_castle[ii-1][j]
                for j in range(M):
                    new_castle[r][j] = 0

            if max_kill < kill:
                max_kill = kill

print(max_kill)