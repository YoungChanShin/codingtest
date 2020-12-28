import sys

sys.stdin = open("input.txt")

def select(relationships, n, m, check_list, s):
    start = -1
    for i in range(s,n):
        if check_list[i]==0:
            start = i
            break
    if start == -1:
        return 1
    cnt = 0
    for j in range(start+1, n):
        if check_list[j] == 0 and relationships[start][j]==1:
            check_list[start] = 1
            check_list[j] = 1
            cnt+=select(relationships, n, m, check_list,start+1)
            check_list[start] = 0
            check_list[j] = 0

    return cnt

for ts in range(int(input())):
    n,m = list(map(int,input().split()))
    data_list = list(map(int, input().split()))
    relationships = [[0]*10 for _ in range(10)]
    for i in range(m):
        relationships[data_list[2*i]][data_list[2*i+1]]=1
        relationships[data_list[2*i+1]][data_list[2*i]]=1
    print(select(relationships, n, m, [0]*n,0))