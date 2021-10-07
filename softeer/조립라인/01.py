import sys
sys.stdin = open('input.txt')

N = int(input())
plan = [list(map(int,input().split())) for _ in range(N)]
# plan[-1].extend([0,0])

dp = [[0]*2 for _ in range(N)] 
dp[0] = plan[0][:2]
for i in range(1, N):
    dp[i][0] = min(dp[i-1][0], dp[i-1][1] + plan[i-1][3]) + plan[i][0]
    dp[i][1] = min(dp[i-1][1], dp[i-1][0] + plan[i-1][2]) + plan[i][1]

print(min(dp[-1]))