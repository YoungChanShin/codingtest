import sys
sys.stdin = open("input.txt")
read = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(cur_i,cur_j):
    global N,M
    stack = [(cur_i,cur_j)]
    while stack:
        _i, _j = stack.pop()
        for d in range(4):
            new_i = _i + dx[d]
            new_j = _j + dy[d]
            if -1<new_i<N and -1<new_j<M and data_list[new_i][new_j]:
                stack.append((new_i, new_j))
                data_list[new_i][new_j] = 0


for ts in range(int(read())):
    N, M, spot = list(map(int,read().split()))
    data_list = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(spot):
        v1, v2 = list(map(int, read().split()))
        data_list[v1][v2] = 1

    for i in range(N):
        for j in range(M):
            if data_list[i][j]: 
                bfs(i,j)
                cnt += 1
    print(cnt)