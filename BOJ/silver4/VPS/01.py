import sys
sys.stdin = open('input.txt')

N = int(input())

for _ in range(N):
    data_list = input()
    cnt = 0
    flag = True
    for p in data_list:
        if p == '(':
            cnt += 1
        elif p == ')':
            cnt -= 1
        if cnt < 0:
            flag = False
            break
    if flag and cnt == 0:
        print('YES')
    else:
        print('NO')