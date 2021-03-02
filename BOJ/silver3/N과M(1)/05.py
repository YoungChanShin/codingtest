import sys
sys.stdin = open('input.txt')

N ,M = list(map(int, input().split()))
data_list = sorted(list(map(int, input().split())))

check_list = [0] * N
answer = [0] * M

def recur(depth):
    global M
    if depth == M:
        print(" ".join(map(str,answer)))
        return
    
    for i in range(N):
        if check_list[i] == 0:
            check_list[i] = 1
            answer[depth] = data_list[i]
            recur(depth+1)
            check_list[i] = 0
            

recur(0)