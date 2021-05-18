import sys
sys.stdin = open('input.txt')

def solution(data_list, L):
    n = len(data_list)
    cnt = 0
    for i in range(n):
        same = 1
        slope = [0]*n # 0이면 경사로를 놓을 수 있는 자리
        for j in range(n):
            if j==n-1:
                cnt += 1
                break
            
            diff = data_list[i][j+1]-data_list[i][j]
            if diff == 0:
                if slope[j] == 0:
                    same += 1
                continue

            same = max(1,same) if slope[j] == 0 else 0
            if diff == 1:
                if same >= L:
                    same = 1
                    continue
                else:
                    break

            if diff == -1:
                flag = True
                if j+L < n:
                    for k in range(j+1,j+L+1):
                        slope[k] = 1
                        if data_list[i][k] != data_list[i][j+1]:
                            flag = False
                            break 
                    if flag:
                        continue

            # 높이차이가 2 이상
            break

    for i in range(n):
        same = 1
        slope = [0]*n # 0이면 경사로를 놓을 수 있는 자리
        for j in range(n):
            if j==n-1:
                cnt += 1
                break
            
            diff = data_list[j+1][i]-data_list[j][i]
            if diff == 0:
                if slope[j] == 0:
                    same += 1
                continue

            same = max(1,same) if slope[j] == 0 else 0
            # same = 1 if slope[j] == 0 else 0 
            if diff == 1:
                if same >= L:
                    same = 1
                    continue
                else:
                    break

            if diff == -1:
                flag = True
                if j+L < n:
                    for k in range(j+1,j+L+1):
                        slope[k] = 1
                        if data_list[k][i] != data_list[j+1][i]:
                            flag = False
                            break 
                    if flag:
                        continue

            # 높이차이가 2 이상
            break
    return cnt


for _ in range(int(input())):
    N, L = list(map(int,input().split()))
    data_list = [list(map(int,input().split())) for _ in range(N)]
    print(solution(data_list, L))