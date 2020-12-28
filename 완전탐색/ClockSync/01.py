'''
2
12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12 
12 9 3 12 6 6 9 3 12 9 12 9 12 12 6 6

0	0, 1, 2
1	3, 7, 9, 11
2	4, 10, 14, 15
3	0, 4, 5, 6, 7
4	6, 7, 8, 10, 12
5	0, 2, 14, 15
6	3, 14, 15
7	4, 5, 7, 14, 15
8	1, 2, 3, 4, 5
9	3, 4, 5, 9, 13


'''
import sys
sys.stdin = open('input.txt')
switches = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]
def isPass(data):
    flag = True
    for i in data:
        if i:
            return False
    return True

def solution(switch_list, data_list, cnt, next_idx):
    print("call",data_list)
    if isPass(data_list) or next_idx>40:
        return cnt
    turn = 9999999
    for i in range(10):
        if switch_list[i] != 0:
            switch_list[i] -= 1
            turn = i
            break
    
    if turn == 9999999:
        return cnt
    print("turn",turn)
    unpick = solution(switch_list,data_list, cnt, next_idx+1)
    for i in switches[turn]:
        data_list[i] = (data_list[i]+3)%12
    pick = solution(switch_list,data_list, cnt+1, next_idx+1)
    return min(pick,unpick)


for ts in range(int(input())):
    data_list = list(map(lambda x: int(x)%12 , input().split()))
    switch_list=[4]*10
    print(solution(switch_list, data_list, 0, 0))



    