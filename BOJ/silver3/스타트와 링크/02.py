import sys
sys.stdin = open('input.txt')
from itertools import combinations

input = sys.stdin.readline
N = int(input())

syn = [list(map(int, input().split())) for _ in range(N)]
side = list(range(1,N))

def calc(check_list):
    star = 0
    link = 0
    for i in range(N):
        if check_list[i]:
            for j in range(N):
                if check_list[j]:
                    star += syn[i][j]
        else:
            for j in range(N):
                if not check_list[j]:
                    link += syn[i][j]
    return abs(star - link)


def comb():
    min_val = 100000
    for i in combinations(side,N//2):
        check_list = [0]*N
        for j in i:
            check_list[j] = 1
        min_val = min(min_val, calc(check_list))
    return min_val

for i in combinations(side,N//2):
    print(i)
print(comb())
