import sys

sys.stdin = open("input.txt")

def solution(plate_size, possiblity, data_list, cur_i, cur_j):
    # 종료 조건
    if possiblity[cur_i][cur_j] == 1:
        return False
    if cur_i == plate_size-1 and cur_j == plate_size-1:
        return True

    new_i = cur_i+data_list[cur_i][cur_j]
    new_j = cur_j+data_list[cur_i][cur_j]

    # 오른쪽으로
    if -1<new_i<plate_size: 
        if solution(plate_size,possiblity,data_list,new_i, cur_j):
            return True

    # 아랫쪽으로
    if -1<new_j<plate_size:
        if solution(plate_size, possiblity, data_list, cur_i, new_j):
            return True

    possiblity[cur_i][cur_j] = 1
    return False



# possiblity 값이 0이면 불가능
for ts in range(1, int(input())+1):
    plate_size = int(input())
    possiblity = [[0]*plate_size for _ in range(plate_size)]
    data_list = [list(map(int, input().split())) for _ in range(plate_size)]
    
    if solution(plate_size, possiblity, data_list,0,0):
        print("YES")
    else:
        print("NO")