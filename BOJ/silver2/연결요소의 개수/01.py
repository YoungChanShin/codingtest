import sys
sys.stdin = open("input.txt")

M, N = list(map(int, input().split()))

data_list = [[] for _ in range(M+1)]
for _ in range(N):
    v1, v2 = list(map(int, input().split()))
    data_list[v1].append(v2)
    data_list[v2].append(v1)

visited = [0]*(M+1)

def bfs(start):
    s = [start]
    while s:
        node = s.pop()
        if visited[node] == 0:
            visited[node] = 1
            s.extend(data_list[node])
# def dfs(v):
#     visited[v] = 1
#     for e in data_list[v]:
#         if not visited[e]:
#             dfs(e)
            

ret = 0
for node in range(1, M+1):
    if visited[node]==0:
        bfs(node)
        ret+=1
print(ret)