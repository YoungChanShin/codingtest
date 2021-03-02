import sys
sys.stdin = open("input.txt")

import math

M,N = list(map(int,input().split()))

check_list = [True]*(N+1)
check_list[1] = False
edge = int(math.sqrt(N+1))
for division in range(2, edge+1):
    if check_list[division]:
        for i in range(2, 1+N//division):
            check_list[division*i] = False

for el in range(M,N+1):
    if check_list[el]:
        print(el)
