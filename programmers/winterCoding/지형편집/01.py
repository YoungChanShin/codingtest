def getTilt(dp, m, P, Q):
    if m>0:
        return dp[m-1]*P - Q*(dp[-1]-dp[m])
    else:
        return -Q*(dp[-1]-dp[m])
def getLeastTilt(dp, l, r, P, Q):
    if l<=r:
        m = (l+r)//2
        mt = getTilt(dp, m, P, Q)
        if mt == 0:
            return m
        elif mt < 0:
            return getLeastTilt(dp, m+1, r, P, Q)
        else:
            return getLeastTilt(dp, l, m-1, P, Q)
    else:
        lt = getTilt(dp, l, P, Q)
        rt = getTilt(dp, r, P, Q)
        # print(">>>>",lt,rt)
        if abs(lt) < abs(rt):
            return l
        return r

def solution(land, P, Q):
    answer = 0
    N = len(land)
    max_val = 0
    min_val = 1000000000
    for i in range(N):
        for j in range(N):
            max_val = max(max_val, land[i][j])
            min_val = min(min_val, land[i][j])
    dp = [0]*(max_val+1)
    for i in range(N):
        for j in range(N):
            dp[land[i][j]] += 1
    
    for i in range(max_val):
        dp[i+1] += dp[i]
    level = getLeastTilt(dp, min_val, max_val, P, Q)
    # print(level)
    for i in range(min_val, max_val+1):
        if i==0:
            # print(P , (level-i) , dp[i])
            answer += P * (level-i) * dp[i]
        elif i-level<0:
            # print(P,(level-i) , (dp[i]-dp[i-1]))
            answer += P*(level-i) * (dp[i]-dp[i-1])
        else:
            # print(Q,(i-level) , (dp[i]-dp[i-1]))
            answer += Q*(i-level) * (dp[i]-dp[i-1])
    return answer

land = [[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]]
land = [[1, 2], [2, 3]]
print(solution(land,3,2))