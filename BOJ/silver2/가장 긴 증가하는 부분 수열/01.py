import sys
sys.stdin = open("input.txt")

N =int(input())
data_list = list(map(int, input().split()))
arr = []
ret = 1

def dfs(cnt, depth):
    global N, ret
    if cnt == N:
        if ret < len(arr):
            ret = len(arr)
        return
    
    for i in range(cnt, N):
        if (len(arr)==0 or arr[-1] <= data_list[i]):
            arr.append(data_list[i])
            dfs(i+1, depth)
            arr.pop(-1)
dfs(0,0)
print(ret)