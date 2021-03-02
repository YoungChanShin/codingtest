import sys
sys.stdin = open("input.txt")

N = int(input())
arr = list(map(int,input().split()))

max_list = [-1000]*N
max_val = arr[0]
max_list[0] = arr[0]
cnt = 0
for i in range(1,N):
    if arr[i]<0:
        if max_list[cnt]<0:
            max_list[cnt] += arr[i]
        else:
            cnt += 1
            max_list[cnt] = arr[i] 
    else:
        if max_list[cnt]>=0:
            max_list[cnt] += arr[i]
        else:
            cnt+=1
            max_list[cnt] = max(arr[i], max_list[cnt-1]+max_list[cnt-2]+arr[i])
    max_val = max(max_val, max_list[cnt], arr[i])
       
# print(max_list)
print(max_val)