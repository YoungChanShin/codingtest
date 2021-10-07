import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def get_dp(root):
    # 0은 자기자신을 포함하지 않는 경우 => 자식 노드 중 자기 자신을 포함하는 거
    visited[root] = 1
    dp[root][0] = 0
    dp[root][1] = 1
    for s in maps[root]:
        if visited[s]==0:
            get_dp(s)
            dp[root][0] += dp[s][1]
            dp[root][1] += min(dp[s])


n = int(input())
dp = [[-1, -1] for _ in range(n+1)]
visited = [0]*(n+1)
maps = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c = list(map(int, input().split()))
    maps[p].append(c)
    maps[c].append(p)

root = 1
get_dp(root)

print(min(dp[1]))

'''
알고리즘을 이해해보자

1. 부모 노드가 얼리어답터이면, 자식 노드들은 최소값들만 모은다
2. 부모 노드가 얼리어답터가 아니면, 자식 노드들은 얼리어답터인 것들을 모은다

두번째 경우에 의문이 든다. 부모가 얼리어답터가 아니면 자식노드 중에서 하나 이상만 얼리어답터이면 되지 않는가?
모두 얼리어답터일 필요는 없지 않는가?? 
    ==> 증명할 수 있는 방법
    증명해야 하는 명제가 무엇인가
        1. 부모가 얼리어답터가 아니면 자식노드가 모두 얼리어답터이어야 한다? ==> 틀린 명제
        2. 반례가 발생한다면,
            1) 부모는 얼리어답터가 아니다.
            2) 이 때, 자식노드가 모두 얼리어답터가 아닌 경우가 최솟값을 가진다.
반례를 찾았다
10
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10



'''