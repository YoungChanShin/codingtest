def getSubset():
    res = []

    def dfs(start=10, arr=[]):
        res.append(arr)

        for i in range(start,-1,-1):
            dfs(i - 1, arr+[i])
    
    dfs()
    return res

def isPosible(c, info, n):
    sum = 0
    for i in c:
        sum += info[i]+1
    return True if sum <= n else False

def calcScore(c, info):
    s = 0
    for i in range(11):
        if i in c:
            s += 10-i
        elif info[i] != 0:
            s -= 10-i
    return s

def solution(n, info):
    answer = []
    candidates = getSubset()
    max_val = -1
    for c in candidates:
        if isPosible(c, info, n):
            s = calcScore(c, info)
            if s > max_val:
                max_val = s
                answer = c
    
    if len(answer) == 0 or max_val == 0:
        return [-1]
    res = [info[s]+1 if s in answer else 0 for s in range(11)]
    if sum(res)< n:
        res[-1] += n-sum(res)
    return res

print(getSubset())