from collections import deque

def valid(r,c,N):
    return 0<=r<N and 0<=c<N 

def solution(board):
    N = len(board)
    visited = [[[0,0] for _ in range(N)] for _ in range(N)]
    q = deque()

    q.append([0,0,0])

    while q:
        r,c,p = q.popleft()
        t = visited[r][c][p]
        if p == 0:
            if r == N-1 and c+1 == N-1:
                return t

            new_r1, new_c1 = r-1, c
            new_r2, new_c2 = r-1, c+1
            if valid(new_r1,new_c1,N) and valid(new_r2,new_c2,N) and board[new_r1][new_c1]==0 and board[new_r2][new_c2]==0:
            # 1. 위로 회전1) 반시계방향
                if visited[r-1][c][1] == 0:
                    q.append([r-1, c, 1])
                    visited[r-1][c][1] = t+1
            # 2. 위로 회전2) 시계방향
                if visited[r-1][c+1][1] == 0:
                    q.append([r-1,c+1,1])
                    visited[r-1][c+1][1] = t+1
            # 3. 위로 평행 이동
                if visited[r-1][c][0] == 0:
                    q.append([r-1,c,0])
                    visited[r-1][c][0] = t+1

            new_r1, new_c1 = r+1, c
            new_r2, new_c2 = r+1, c+1
            if valid(new_r1,new_c1,N) and valid(new_r2,new_c2,N) and board[new_r1][new_c1]==0 and board[new_r2][new_c2]==0:
            # 4. 아래로 회전1) 시계방향
                if visited[r][c][1] == 0:
                    q.append([r, c, 1])
                    visited[r][c][1] = t+1
            # 5. 아래로 회전2) 반시계방향
                if visited[r][c+1][1] == 0:
                    q.append([r,c+1,1])
                    visited[r][c+1][1] = t+1
            # 6. 아래로 평행이동
                if visited[r+1][c][0] == 0:
                    q.append([r+1,c,0])
                    visited[r+1][c][0] = t+1
            
            # 7. 오른쪽으로 평행이동
            new_r, new_c = r, c+2
            if valid(new_r, new_c,N) and board[new_r][new_c] == 0:
                if visited[r][c+1][0] == 0:
                    q.append([r,c+1,0])
                    visited[r][c+1][0] = t+1

            # 8. 왼쪽으로 평행이동
            new_r, new_c = r, c-1
            if valid(new_r,new_c,N) and board[new_r][new_c] == 0:
                if visited[r][c-1][0] == 0:
                    q.append([r,c-1,0])
                    visited[r][c-1][0] = t+1
            
        else:
            if r+1 == N-1 and c == N-1:
                return t
            new_r1, new_c1 = r, c+1
            new_r2, new_c2 = r+1, c+1
            if valid(new_r1,new_c1,N) and valid(new_r2,new_c2,N) and board[new_r1][new_c1]==0 and board[new_r2][new_c2]==0:
            # 1. 오른쪽으로 회전1) 반시계방향
                if visited[r][c][0] == 0:
                    q.append([r, c, 0])
                    visited[r][c][0] = t+1
            # 2. 오른쪽으로 회전2) 시계방향
                if visited[r+1][c][0] == 0:
                    q.append([r+1,c,0])
                    visited[r+1][c][0] = t+1
            # 3. 오른쪽으로 평행이동
                if visited[r][c+1][1] == 0:
                    q.append([r,c+1,1])
                    visited[r][c+1][1] = t+1

            new_r1, new_c1 = r, c-1
            new_r2, new_c2 = r+1, c-1
            if valid(new_r1,new_c1,N) and valid(new_r2,new_c2,N) and board[new_r1][new_c1]==0 and board[new_r2][new_c2]==0:
            # 4. 왼쪽으로 회전1) 시계방향
                if visited[r][c-1][0] == 0:
                    q.append([r, c-1, 0])
                    visited[r][c-1][0] = t+1
            # 5. 왼쪽으로 회원2) 반시계방향
                if visited[r+1][c-1][0] == 0:
                    q.append([r+1,c-1,0])
                    visited[r+1][c-1][0] = t+1
            # 6. 왼쪽으로 평행이동
                if visited[r][c-1][1] == 0:
                    q.append([r,c-1,1])
                    visited[r][c-1][1] = t+1
            # 7. 위로 평행이동
            new_r, new_c = r-1, c
            if valid(new_r, new_c,N) and board[new_r][new_c] == 0:
                if visited[r-1][c][1] == 0:
                    q.append([r-1,c,1])
                    visited[r-1][c][1] = t+1
            # 8. 아래로 평행이동 
            new_r, new_c = r+2, c
            if valid(new_r,new_c,N) and board[new_r][new_c] == 0:
                if visited[r+1][c][1] == 0:
                    q.append([r+1,c,1])
                    visited[r+1][c][1] = t+1

    return 0


# board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
board = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]

print(solution(board))