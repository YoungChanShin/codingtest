import sys
from itertools import permutations
from copy import deepcopy
sys.stdin = open('input.txt')

input = sys.stdin.readline

def rotate(data_list,r,c,size):
    r_start = r-size-1
    c_start = c-size-1
    r_end = r+size-1
    c_end = c+size-1

    base = data_list[r_start][c_start]
    for i in range(size*2):
        data_list[r_start+i][c_start] = data_list[r_start+i+1][c_start]
    
    for i in range(size*2):
        data_list[r_end][c_start+i] = data_list[r_end][c_start+i+1]
    
    for i in range(size*2):
        data_list[r_end-i][c_end] = data_list[r_end-i-1][c_end]
    
    for i in range(size*2):
        data_list[r_start][c_end-i] = data_list[r_start][c_end-i-1]
    
    data_list[r_start][c_start+1] = base
 
r, c, s = list(map(int, input().split()))
data_list = [list(map(int, input().split())) for _ in range(r)]
   
rotation_comb = []   
for _ in range(s):
    rotation_comb.append(list(map(int, input().split())))

rotation_comb = permutations(rotation_comb, s)
answer = float('inf')

for comb in rotation_comb:
    new_data_list = deepcopy(data_list)

    for r_s, c_s, size in comb:
        for t in range(size,0,-1):
            rotate(new_data_list,r_s,c_s,t)

    for d in new_data_list:
        sumation = sum(d)
        if sumation < answer:
            answer = sumation

print(answer)