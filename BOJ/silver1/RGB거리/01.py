import sys
sys.stdin = open("input.txt")

N = int(input())
dp = [[0,0,0] for _ in range(N)]
rgb = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1]+rgb[i][0], dp[i-1][2]+rgb[i][0])

    dp[i][1] = min(dp[i-1][0]+rgb[i][1], dp[i-1][2]+rgb[i][1])

    dp[i][2] = min(dp[i-1][0]+rgb[i][2], dp[i-1][1]+rgb[i][2])

print(min(dp[N-1]))