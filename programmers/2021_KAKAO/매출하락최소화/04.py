def calc(maps, sales,  dp, visited, root):
    _child = []
    dp[root][0] = sales[root] # 팀장 창
    dp[root][1] = 0   # 팀장 불참
    flag = False                # 팀원 불참
    if len(maps[root])==0:
        return
    _cnt = 0
    for s in maps[root]:
        calc(maps, sales, dp, visited, s)
        if dp[s][0] <= dp[s][1]:    # 특정 팀원이 이끄는 팀에서 팀원이 참가하기로 한 경우
            _cnt += dp[s][0]
            flag = True
        else:                       # 특정 팀원이 이끄는 팀에서 팀원이 참가하지 않는 경우
            _cnt += dp[s][1]
        _child.append(dp[s])

    dp[root][0] += _cnt
    if flag:                        # 팀장이 불참하는데 팀원 중에 참여자가 있는 경우
        dp[root][1] = _cnt

    else:                           # 팀장이 불참하는데 어떤 팀원도 참여하지 않는 경우
        # 기회비용이 가장 작은 팀에서 팀장이 참여를 결정해야 한다.
        diff = float('inf')
        staff = -1
        _cnt = 0
        for s_id, s in enumerate(_child):
            _cnt += s[1]
            if diff > s[0]-s[1]:
                staff = s_id
                diff = s[0]-s[1]
        dp[root][1] = _cnt + diff


def solution(sales, links):
    n = len(sales)
    maps = [[] for _ in range(n)]
    for b, s in links:
        maps[b-1].append(s-1)
    dp = [[0,0] for _ in range(n)]
    calc(maps, sales, dp, visited, 0)
    return min(dp[0])

sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]

sales = [10, 10, 1, 1]
links = [[3,2], [4,3], [1,4]]
print(solution(sales, links))