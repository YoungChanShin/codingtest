copy_board = [[0]*5 for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
N,M = 0,0
dr = [0,0,1,-1]
dc = [1,-1,0,0]

def valid(r,c):
    global N,M
    return r<0 or N-1<r or c<0 or M-1<c

def solve(my_r, my_c, op_r, op_c):
    global copy_board, visited, N, M
    ret = 0

    if visited[my_r][my_c] == 1: return 0

    for i in range(4):
        val = 0
        new_r = my_r + dr[i]
        new_c = my_c + dc[i]

        if valid(new_r, new_c) or copy_board[new_r][new_c] == 0 or visited[new_r][new_c] == 1:
            continue


        visited[my_r][my_c] = 1
        val = solve(op_r, op_c, new_r, new_c) + 1 # 이번 경로를 택했을 때 결과값
        this_path = val % 2 # 홀수이면 이번 경로를 선택했을 때 나의 승리
        total_path = ret % 2 # 홀수이면 내가 이길 방법이 있다는 뜻
        if this_path == 1 and total_path == 1: ret = min(ret, val)
        elif this_path == 1 and total_path == 0: ret = val
        elif this_path == 0 and total_path == 0: ret = max(ret, val)

        visited[my_r][my_c] = 0
    return ret 


def solution(board, aloc, bloc):
    global copy_board, visited, N, M
    N = len(board)
    M = len(board[0])
    for i in range(N):
        for j in range(M):
            copy_board[i][j] = board[i][j]
    return solve(aloc[0], aloc[1], bloc[0], bloc[1])

block = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]

print(solution(block, aloc, bloc))