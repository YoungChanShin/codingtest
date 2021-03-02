import sys
sys.stdin = open("input.txt")

N = int(input())

dp = [[0]*(10) for _ in range(N+1)]
for i in range(10):
    dp[1][i] = 1

for i in range(2,N+1):
    for j in range(10):
        if j==0:
            dp[i][j] = 1
        else:
            dp[i][j]= dp[i-1][j] + dp[i][j-1]

print(sum(dp[N])%10007)

'''
k=int(input())
result=1
for i in range(9+k,9,-1):
    result*=i
for i in range(1,k+1):
    result//=i
print(result%10007)
'''