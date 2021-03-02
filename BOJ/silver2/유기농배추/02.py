import sys
sys.stdin = open("input.txt")

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
            if -1<new_i<N and -1<new_j<M and (new_i,new_j) in data_list:
                stack.append((new_i, new_j))
        if (_i, _j) in data_list:
            data_list.remove((_i, _j))


for ts in range(int(input())):
    N, M, spot = list(map(int,input().split()))
    data_list = [tuple(map(int, input().split())) for _ in range(spot)]
    cnt = 0
    while data_list:
        i, j = data_list.pop()
        bfs(i,j)
        cnt += 1
    
    print(cnt)