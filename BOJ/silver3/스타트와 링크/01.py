import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())

syn = [list(map(int, input().split())) for _ in range(N)]

side = [0]*N
side[0] = 1

def calc():
    answer = 0
    star = 0
    link = 0
    for i in range(N):
        if side[i]:
            for j in range(N):
                if side[j]:
                    star += syn[i][j]
        else:
            for j in range(N):
                if not side[j]:
                    link += syn[i][j]
    return abs(star - link)

    return answer


def comb(cnt,select):

    min_val = 10000
    # 선택해야 하는 갯수 :  N//2 - select
    # 선택할 수 있는 갯수 : N-cnt
    if N//2 - select > N-cnt:
        return min_val

    if select == N//2:
        return calc()

    for i in range(cnt,N):
        min_val = min(min_val, comb(i+1,select))
        side[i] = 1
        min_val = min(min_val, comb(i+1,select+1))
        side[i] = 0
    return min_val

print(comb(1,1))