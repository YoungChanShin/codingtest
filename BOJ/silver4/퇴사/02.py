import sys
sys.stdin = open("1.txt")

def solution(nthDate):
    global N
    if nthDate == N:
        return 0
    else:
        # 포함
        a = 0 
        if nthDate + data_list[nthDate][0]<=N:
            a = solution(nthDate+data_list[nthDate][0]) + data_list[nthDate][1]
        # 불포함
        b = solution(nthDate+1)
        return max(a,b)

N = int(input())
data_list = [tuple(map(int, input().split())) for _ in range(N)]
print(solution(0))