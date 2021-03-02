import sys
sys.stdin = open("input.txt")

N =int(input())
data_list =[0] + list(map(int, input().split()))
dp = [0]*(N+1)
ret = 1
for i in range(1, N+1):
    small = 0
    for j in range(i):
        if data_list[i]>data_list[j]:
            if small<dp[j]:
                small = dp[j]
    dp[i] = small+1
    if ret<dp[i]:
        ret = dp[i]

print(ret)