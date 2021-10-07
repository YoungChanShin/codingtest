def calc(maps, sales,  dp, root):
    _cnt = 0
    diff = float('inf')
    dp[root][0] = sales[root]
    for s in maps[root]:
        calc(maps, sales, dp, s)
        if dp[s][0]<dp[s][1]:   # 팀원이 참석
            _cnt += dp[s][0]
            diff = 0
        else:                   # 팀원의 팀원이 참석
            _cnt += dp[s][1]
            if diff > dp[s][0] - dp[s][1]:
                diff = dp[s][0] - dp[s][1]
    if diff == float('inf'):
        diff = 0
        
    dp[root] = [_cnt+sales[root], _cnt+diff]

def solution(sales, links):
    n = len(sales)
    maps = [[] for _ in range(n)]
    for b, s in links:
        maps[b-1].append(s-1)
    dp = [[0,0] for s in range(n)]
    calc(maps, sales, dp, 0)
    return min(dp[0])

sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]

sales = [10, 10, 1, 1]
links = [[1,2], [2,3], [3,4]]
print(solution(sales, links))