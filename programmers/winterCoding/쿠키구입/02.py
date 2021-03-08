def binary(dp, l, r, ll, rr, answer):
    if ll<=rr:
        m = (ll+rr)//2
        if dp[m]-dp[l-1] == dp[r]-dp[m]:
            return dp[m]-dp[l-1]

        if dp[m]-dp[l-1] < dp[r]-dp[m]:
            if answer > dp[r]-dp[m]:
                return -1
            return binary(dp, l, r, m+1, rr, answer)

        if dp[m]-dp[l-1] > dp[r]-dp[m]:
            if answer > dp[m]-dp[l-1]:
                return -1
            return binary(dp, l, r, ll, m-1, answer)
    else:
        return -1
    


def solution(cookie):
    answer = 0
    N = len(cookie)
    dp = [0]*(N+1)
    for i in range(N):
        dp[i+1] = dp[i]+cookie[i]
    for l in range(N):
        for r in range(l+1, N+1):
            m = (l+r)//2
            answer = max(answer, binary(dp, l, r, l, r, answer))
    return answer