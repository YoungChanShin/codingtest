from collections import deque

dr = [1,0,-1,0]
dc = [0,1,0,-1]
N = 0
def valid(r,c):
    return 0<=r<N and 0<=c<N

def solution(board):
    global N
    answer = float('inf')
    N = len(board)
    visited = [[float('inf') for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append([0,0,-1,0])
    
    while q:
        r,c,p,f = q.popleft()
        if f==float('inf'):
            continue
        if r == N-1 and c == N-1 and answer > f:
            answer = f

        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if not valid(new_r, new_c) or board[new_r][new_c]==1:
                continue
            cost = f + (100 if i == p or p == -1 else 600)
            if visited[new_r][new_c] >= cost:
                q.append([new_r, new_c, i, cost])
                visited[new_r][new_c] = cost
                
    return answer

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

print(solution(board))