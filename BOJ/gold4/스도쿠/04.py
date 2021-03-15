import sys
sys.stdin = open('input.txt')
from collections import deque

input = sys.stdin.readline

suduku = [list(map(int,input().split())) for _ in range(9)]
q = deque()
for i in range(9):
    for j in range(9):
        if suduku[i][j]==0:
            q.append((i,j))

def isValid(r,c):
    check_list = [0]*10
    for i in range(9):
        check_list[suduku[r][i]] = 1
    
    for i in range(9):
        check_list[suduku[i][c]] = 1
    
    for i in range(r//3*3, r//3*3+3):
        for j in range(c//3*3, c//3*3+3):
            check_list[suduku[i][j]] = 1
    answer = []
    for i in range(1,10):
        if check_list[i]==0:
            answer.append(i)
    return answer

flag = False
def dfs(cnt):
    global flag
    if flag:
        return

    if cnt == len(q):
        flag = True
        for i in suduku:
            print(*i)
        return
    
    r,c = q[cnt]
    promise = isValid(r,c)
    for p in promise:
        suduku[r][c] = p
        dfs(cnt + 1)
        suduku[r][c] = 0

                
dfs(0)

