import sys
sys.stdin = open("input.txt")

def solution(cur_i, cur_j):
    global plate_size

    if cur_i>=plate_size or cur_j >= plate_size:
        return False
    if cur_i == plate_size-1 and cur_j == plate_size -1 :
        return True
    
    if possiblity[cur_i][cur_j] == -1:
        return False
    if solution(cur_i+data_list[cur_i][cur_j],cur_j) or solution(cur_i, cur_j+data_list[cur_i][cur_j]):
        return True
    possiblity[cur_i][cur_j] = -1
    return False

for ts in range(1, 1+int(input())):
    plate_size = int(input())
    possiblity = [[0]*plate_size for _ in range(plate_size)]
    data_list = [list(map(int, input().split())) for _ in range(plate_size)]
    if solution(0,0):
        print("YES")
    else:
        print("NO")