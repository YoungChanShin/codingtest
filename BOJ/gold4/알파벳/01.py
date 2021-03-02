import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

di = [0,0,-1,1]
dj = [1,-1,0,0]

R,C = list(map(int, input().split()))
board = [input() for _ in range(R)]
visited = [0]*26
visited[ord(board[0][0])-65] = 1
max_val = 0
def dfs(r,c,cnt):
    global max_val
    max_val = max(max_val, cnt)
    for i in range(4):
        new_i = r + di[i]
        new_j = c + dj[i]
        if -1<new_i<R and -1<new_j<C and visited[ord(board[new_i][new_j])-65] == 0:
            visited[ord(board[new_i][new_j])-65] = 1
            dfs(new_i, new_j, cnt+1)
            visited[ord(board[new_i][new_j])-65] = 0

dfs(0,0,1)
print(max_val)