import sys
sys.stdin = open("input.txt")

N, M = list(map(int, input().split()))
data_list = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]

def bfs():
    q = [(0,0,1)]

    while q:
        row, col, cnt = q.pop(0)

        for direction in range(4):
            new_row = row+di[direction]
            new_col = col+dj[direction]
            if -1<new_row<N and -1<new_col<M and visited[new_row][new_col]==0 and data_list[new_row][new_col]=='1':
                if new_row+1 == N and new_col+1 == M:
                    return cnt+1
                visited[new_row][new_col] = 1
                q.append((new_row, new_col, cnt+1))

print(bfs())