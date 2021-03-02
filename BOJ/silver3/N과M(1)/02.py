import sys
sys.stdin = open("input.txt")

N, M = list(map(int,input().split()))
# 4 2

def search(cnt, check_list, remain):
    global N,M
    if remain == 0:
        print(check_list)
        return
    elif remain < 1 or cnt>N:
        return
    
    new_check_list = check_list[:]
    while remain>0 or cnt<=N:

        search(cnt+1, new_check_list, remain)
    
        remain -= 1 
        new_check_list[cnt] += 1

        search(cnt, new_check_list, remain)

search(1,[0]*(N+1), M)