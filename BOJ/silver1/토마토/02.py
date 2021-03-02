import sys
from collections import deque
# input = sys.stdin.readline
sys.stdin = open("input.txt")

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
 
def solve(haveto):

    res = 0
    while tmt and haveto:
        l = len(tmt)
        for _ in range(l):
            x, y = tmt.popleft()
            for i in range(4):
                new_x = x+di[i]
                new_y = y+dj[i]
                if -1<new_x<n and -1<new_y<m and tomato[new_x][new_y]=='0':
                    tomato[new_x][new_y] = 1
                    tmt.append((new_x,new_y))
                    haveto -=1
                
        res += 1
    if haveto:
        print(-1)
    else:
        print(res)


m, n = map(int, input().split())
tomato = []
haveto = 0
tmt = deque()
for i in range(n):
    tomato.append(input().split())
    for j in range(m):
        if tomato[i][j] == '0':
            haveto += 1
        elif tomato[i][j] == '1':
            tmt.append((i, j))
solve(haveto)