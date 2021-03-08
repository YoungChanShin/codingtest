def solution(cookie):
    answer = 0
    N = len(cookie)
    dp = [0]*(N+1)
    for i in range(N):
        dp[i+1] = dp[i]+cookie[i]
    print(dp)
    for l in range(N):
        for r in range(l+1, N+1):
            for m in range(l,r):
                if dp[m]-dp[l-1] == dp[r]-dp[m]:
                    answer = max(answer, dp[r]-dp[m])
    return answer

