import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

suduku = [list(map(int,input().split())) for _ in range(9)]
back_tracking = [[[] for i in range(9)] for j in range(9)]

def whatIsit(r,c):
    check_list = [0]*10
    check_list[0] = 1
    cnt = 0
    for i in range(9):
        if check_list[suduku[r][i]] == 0:
            check_list[suduku[r][i]] = 1
            cnt += 1
    if cnt == 8:
        for i in range(1,10):
            if check_list[i]==0:
                return i

    for i in range(9):
        if check_list[suduku[i][c]] == 0:
            check_list[suduku[i][c]] = 1
            cnt += 1
    if cnt == 8:
        for i in range(1,10):
            if check_list[i]==0:
                return i

    for i in range((r//3)*3,(r//3)*3+3):
        for j in range((c//3)*3, (c//3)*3+3):
            if check_list[suduku[i][j]] == 0:
                check_list[suduku[i][j]] = 1
                cnt += 1
    if cnt == 8:
        for i in range(1,10):
            if check_list[i]==0:
                return i

    for i in range(1,10):
        if check_list[i] == 0:
            back_tracking[r][c].append(i)
    return 0
    
flag = True
while flag:
    flag = False
    for i in range(9):
        for j in range(9):
            if suduku[i][j] == 0:
                ret = whatIsit(i,j)
                if ret != 0:
                    suduku[i][j] = ret
                flag = True
    
for i in suduku:
    print(*i)