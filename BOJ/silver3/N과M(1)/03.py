import sys
sys.stdin = open("input.txt")

N, M = list(map(int,input().split()))
# 4 2
check_list = [0]*M

def search(cnt, depth):
    global N,M
    if depth == M:
        for i in check_list:
            print(i, end=" ")
        print()
        return
    
    for i in range(cnt, N+1):
        check_list[depth] = i
        search(i, depth+1)

search(1, 0)