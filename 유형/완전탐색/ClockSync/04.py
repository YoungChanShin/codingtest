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

def solution(n, data_list, cnt,call):
    # print(data_list)
    if cnt>9:
        return 0 if isPass(data_list) else 999999
    ret = 999999
    for i in range(4):
        pick = i+solution(n,data_list, cnt+1, call)
        for j in switches[cnt]:
            data_list[j] = (data_list[j]+3)%12
        if -1 < pick and pick < call:
            call = pick
    return call
    
for ts in range(int(input())):
    data_list = list(map(lambda x: int(x)%12 , input().split()))
    check_list = [0]*10
    print(solution(10, data_list, 0, -1))



    