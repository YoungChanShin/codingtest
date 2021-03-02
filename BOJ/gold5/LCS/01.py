# 틀린 코드입니다
# 왜 틀렸는지는 모르겠습니다.

import sys
sys.stdin = open('input.txt')

str1 = input()
str2 = input()
N = len(str1)
M = len(str2)

compare = [[0]*N for _ in range(M)]
dp = [0]*N
for i in range(M):
    for j in range(N):
        if str2[i] == str1[j]:
            if j>0:
                compare[i][j] = max(dp[:j])+1
            else:
                compare[i][j] = 1
    for j in range(N):
        if compare[i][j]>dp[j]:
            dp[j] = compare[i][j]
# for i in compare:
#     print(i)
# print(dp)
print(max(dp))