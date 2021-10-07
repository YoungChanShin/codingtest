import sys
sys.stdin = open('input.txt')

N, K = list(map(int,input().split()))
plan = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*K for _ in range(N)] 
dp[0] = plan[0][:K]
#  Li, j 작업장에서 Lk, j+1 (k ≠ i) 작업장까지 이동시간이 i의 오름차순(i가 동일할 때는 k의 오름차순)으로 주어진다.
for i in range(1, N):
    # dp[i][0] = min(dp[i-1][0], dp[i-1][1] + plan[i-1][3]) + plan[i][0]
    # dp[i][1] = min(dp[i-1][1], dp[i-1][0] + plan[i-1][2]) + plan[i][1]
    min_val = 100000
    for j in range(K):
        shift = plan[i-1][K + (K -1) * j:K + (K - 1) * (j+1)]
        for k in range(K):
            if k == j:
                min_val = min(min_val, dp[i-1][k])

            elif k < j:
                print(i,j,k,shift, "down")
                min_val = min(min_val, dp[i-1][k-1] + shift[j-1])
            elif k > j:
                print(i,j,k,shift, "up")
                min_val = min(min_val, dp[i-1][k] + shift[j])
        print(min_val)

    
        dp[i][j] = min_val + plan[i][j]
print(dp)
print(min(dp[-1]))