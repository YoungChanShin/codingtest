import sys
from sys import stdin

sys.setrecursionlimit(10**9)

def DFS(cur):
    visited[cur] = True
    for i in edges[cur]:
        if not visited[i]:
            child[cur].append(i)
            DFS(i)

def get_dp(cur, check):
    if check: # 얼리어답터면
        # DP( i, true) = min(DP(i 의 자식, true), DP(i 의 자식, false))들의 총합 + 1
        if dp[cur][1] != -1:
            return dp[cur][1]
        dp[cur][1] = 1 # 본인이 얼리어답터니 + 1을 해주는 것이다.
        for i in child[cur]: # 하위 노드 탐색
            dp[cur][1] += min(get_dp(i, False), get_dp(i, True))
        return dp[cur][1]
    else: # 얼리어답터가 아니며
        # DP( i, false) = DP(i 의 자식, true) 들의 총합 
        if dp[cur][0] != -1:
            return dp[cur][0]
        dp[cur][0] = 0 # 얼리어답터가 아니므로 0
        for i in child[cur]: # 하위 노드 탐색
            dp[cur][0] += get_dp(i, True) #
        return dp[cur][0]


stdin = open("input.txt", "r")

# N 노드의 개수
N = int(stdin.readline()) 

edges = [[] for _ in range(N+1)]
child = [[] for _ in range(N+1)]

# (u, v) N-1개
for _ in range(N-1):
    u, v = map(int, stdin.readline().rstrip().split())
    # 양방향 추가
    edges[u].append(v)
    edges[v].append(u)

dp = [[-1, -1] for _ in range(N+1)] # dp 초기화
visited = [False] * (N+1)

print(min(get_dp(1, False), get_dp(1, True)))

print(dp)