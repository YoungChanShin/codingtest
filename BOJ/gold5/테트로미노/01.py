import sys
sys.stdin = open("input.txt")

input = sys.sydin.readline

di = [[0,0,0,0],[0,1,2,3],[0,0,0,1],[0,1,2,2],[0,1,2,2],[0,1,1,1],[0,0,0,1],[0,1,2,0],[1,1,1,0],[0,0,1,2],[0,1,1,2],[1,1,0,0],[0,0,1,1],[0,1,1,2],[0,1,1,2],[0,1,1,1],[0,1,1,2],[0,0,0,1],[0,1,1,0]]
dj = [[0,1,2,3],[0,0,0,0],[0,1,2,2],[1,1,1,0],[0,0,0,1],[0,0,1,2],[0,1,2,0],[0,0,0,1],[0,1,2,2],[0,1,1,1],[0,0,1,1],[0,1,1,2],[0,1,1,2],[1,0,1,0],[0,0,1,0],[1,0,1,2],[1,0,1,1],[0,1,2,1],[0,1,0,1]]
num_of_type = len(di)

N,M = list(map(int,input().split()))
paper = [list(map(int,input().split())) for _ in range(N)]

max_s = 0
for i in range(N):
    for j in range(M):
        for k in range(num_of_type):
            s = 0
            for a in range(4):
                new_i = i+di[k][a]
                new_j = j+dj[k][a]
                if -1<new_i<N and -1<new_j<M:
                    s += paper[new_i][new_j]
                    if a == 3 and max_s<s:
                        max_s = s
                else:
                    break
print(max_s)