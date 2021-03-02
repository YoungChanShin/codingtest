import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

di = [0,0,-1,1]
dj = [1,-1,0,0]

R,C = list(map(int, input().split()))
board = [input() for _ in range(R)]
check_board = [[-1]*C for _ in range(R)]
# check_board[0][0] = 1
visited = [0]*26
visited[ord(board[0][0])-65] = 1

def dfs(r,c):
    cnt = 0
    for i in range(4):
        new_i = r + di[i]
        new_j = c + dj[i]
        if -1<new_i<R and -1<new_j<C and visited[ord(board[new_i][new_j])-65] == 0:
            visited[ord(board[new_i][new_j])-65] = 1
            cnt = max(cnt, dfs(new_i, new_j))
            visited[ord(board[new_i][new_j])-65] = 0
    check_board[r][c] = cnt
    return cnt + 1

ret = dfs(0,0)
print(ret)