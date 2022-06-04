# [참고] : https://blog.encrypted.gg/1032
# [출처] : https://github.com/encrypted-def/kakao-blind-recruitment/blob/master/2022-blind/Q7.py

dr = [0,0,1,-1]
dc = [1,-1,0,0]

visited = [[0]*5 for _ in range(5)]
copy_board = [[0]*5 for _ in range(5)]
N,M = 0,0

def valid(r,c):
    global N,M
    return r<0 or r>N-1 or c<0 or c>M-1

def solve(myr, myc, urr, urc):
    global visited, copy_board
    if visited[myr][myc] == 1:
        return 0
    ret = 0
    for i in range(4):
        new_r = myr+ dr[i]
        new_c = myc+ dc[i]
        if valid(new_r, new_c) or visited[new_r][new_c] == 1 or copy_board[new_r][new_c] == 0: continue

        # 이동
        visited[myr][myc] = 1

        val = solve(urr, urc, new_r, new_c) + 1

        if ret % 2 == 0 and val % 2 == 1: 
            ret = val
        elif ret % 2 == 0 and val % 2 == 0: 
            ret = max(ret, val) 
        elif ret % 2 == 1 and val % 2 == 1:
            ret = min(ret,val)
        
        visited[myr][myc] = 0

    return ret

def solution(board, aloc, bloc):
    global visited, copy_board, N, M
    N = len(board)
    M = len(board[0])

    for i in range(N):
        for j in range(M):
            copy_board[i][j] = board[i][j]
    
    return solve(aloc[0],aloc[1],bloc[0],bloc[1])


board = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]

# board = [[1, 1, 1, 1, 1]]
# aloc = [0,0]
# bloc = [0,4]

print(solution(board, aloc, bloc))