from queue import PriorityQueue

dr = [0,0,1,-1]
dc = [1,-1,0,0]


def solution(board):
    answer = 0
    N = len(board)
    visited = [[[float('inf')]*4 for _ in range(N)] for _ in range(N)]
    q = PriorityQueue()
    def valid(r,c):
        return 0<=r<N and 0<=c<N

    visited[0][1][0] = 100
    q.put((100,0,1,0))
    visited[1][0][3] = 100
    q.put((100,1,0,3))

    while q.qsize() > 0:
        f,r,c,d = q.get()
        if r == N-1 and c == N-1 and f > answer:
            answer = f
        
        for i in range(4):
            new_r = r+ dr[i]
            new_c = c+ dc[i]
            if not valid(new_r,new_c):
                continue
            if board[new_r][new_c] == 1:
                continue
            cost = f + (100 if i == d else 600)
            if visited[new_r][new_c][i] > cost:
                visited[new_r][new_c][i] = cost
                q.put((cost,new_r, new_c,i))

    return answer

board = [[0,0,0],[0,0,0],[0,0,0]]

print(solution(board))