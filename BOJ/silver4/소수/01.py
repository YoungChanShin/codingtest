import sys
sys.stdin = open('input.txt')

M = int(input())
N =int(input())
check_list = [1]*(N+1)
check_list[1] = 0
import math

start = int(math.sqrt(N))
for i in range(2, start+1):
    if check_list[i]:
        how_many = N//i
        for j in range(2,how_many+1):
            check_list[i*j]=0
cnt = 0
min_val = -1

for i in range(M,N+1):
    if check_list[i]:
        if min_val==-1:
            min_val = i
        cnt+=i

if min_val!=-1:
    print(cnt)
print(min_val)