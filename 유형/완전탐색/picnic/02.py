import sys

sys.stdin = open("input.txt")
'''
안되는 코드입니다
'''
def select(relationships, n, m, check_list, s):
    cnt = 0
    if sum(check_list)==n:
        return 1
    start = -1
    for i in range(s,n):
        if check_list[i]==0:
            start = i
            for j in range(m):
                if (relationships[j][0] == start and check_list[relationships[j][1]]) or (relationships[j][1] == start and check_list[relationships[j][0]])== 0:
                    check_list[start] = 1
                    check_list[relationships[j][1]] = 1
                    cnt += select(relationships, n, m, check_list,start)
                    check_list[start] = 0
                    check_list[relationships[j][1]] = 0
    return cnt

for ts in range(int(input())):
    n,m = list(map(int,input().split()))
    data_list = list(map(int, input().split()))
    relationships = [[data_list[2*i],data_list[2*i+1]] for i in range(m)]
    print(select(relationships, n, m, [0]*n,0))