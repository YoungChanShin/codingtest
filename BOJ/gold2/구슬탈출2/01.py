import sys
sys.stdin = open("input.txt")
from copy import deepcopy

input = sys.stdin.readline

N,M = list(map(int,input().split()))
board = [list(input()) for _ in range(N)]
record = [0]*11
min_ret = 0
# -2: 좌, 2: 우, -1: 상 ,1: 하
def move(direction, new_board):
    r=[]
    b=[]
    for i in range(N):
        for j in range(M):
            if new_board[i][j]=="R":
                r = [i,j]
            if new_board[i][j]=="B":
                b = [i,j]

    if direction == -2:
        if r[0]==b[0]:
            if r[1] < b[1]:
                # red 옮기기
                new_board[r[0]][r[1]] = '.'
                while 0<r[1] and new_board[r[0]][r[1]-1] =='.':
                    r[1] -= 1
                    if new_board[r[0]][r[1]] =='O':
                        return 0
                new_board[r[0]][r[1]] = 'R'

                # blue 옮기기
                new_board[b[0]][b[1]] = '.'
                while 0<b[1] and new_board[b[0]][b[1]-1] =='.':
                    b[1] -= 1
                    if new_board[b[0]][b[1]] =='O':
                        return -1
                new_board[b[0]][b[1]] = 'B'
            else:
                # blue 옮기기
                new_board[b[0]][b[1]] = '.'
                while 0<b[1] and new_board[b[0]][b[1]-1] =='.':
                    b[1] -= 1
                    if new_board[b[0]][b[1]] =='O':
                        return -1
                new_board[b[0]][b[1]] = 'B'
                # red 옮기기
                new_board[r[0]][r[1]] = '.'
                while 0<r[1] and new_board[r[0]][r[1]-1] =='.':
                    r[1] -= 1
                    if new_board[r[0]][r[1]] =='O':
                        return 0
                new_board[r[0]][r[1]] = 'R'
        else:
            # blue 옮기기
            new_board[b[0]][b[1]] = '.'
            while 0<b[1] and new_board[b[0]][b[1]-1] =='.':
                b[1] -= 1
                if new_board[b[0]][b[1]] =='O':
                    return -1
            new_board[b[0]][b[1]] = 'B'
            # red 옮기기
            new_board[r[0]][r[1]] = '.'
            while 0<r[1] and new_board[r[0]][r[1]-1] =='.':
                r[1] -= 1
                if new_board[r[0]][r[1]] =='O':
                    return 0
            new_board[r[0]][r[1]] = 'R'
        return new_board





    return new_board

def solution(depth, this_board):
    global min_ret
    ret = 0
    if depth==11:
        return -1
    

    for i in (-2,-1,1,2):
        if i != -record[depth-1] and i != record[depth-1]:
            # if i 방향으로 한칸도 이동하지 못할 경우: 종료하기
            new_board = deepcopy(this_board)
            record[depth] = i
            temp = move(i, new_board)
            if temp == -1:
                continue
            if temp == 0:
                return depth
            ret = solution(depth+1,temp)
            if ret>0:
                min_ret = min(ret, min_ret)
    return min_ret


print(solution(1, board))