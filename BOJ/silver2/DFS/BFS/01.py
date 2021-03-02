import sys
sys.stdin = open("input.txt")

E, V, start = list(map(int,input().split()))
data_list = [[] for _ in range(E+1)]
for _ in range(V):
    e1,e2 = list(map(int, input().split())) 
    data_list[e1].append(e2)
    data_list[e2].append(e1)

def bfs():
    bfs_queue = [start]
    visited = []
    while len(bfs_queue) != 0:
        n = bfs_queue.pop(0)
        if n not in visited:
            visited.append(n)
            bfs_queue.extend(sorted(data_list[n]))
            print(n, end=" ")
    print()

def dfs():
    dfs_stack = [start]
    visited = []
    while len(dfs_stack) != 0:
        n = dfs_stack.pop(-1)
        if n not in visited:
            visited.append(n)
            dfs_stack.extend(sorted(data_list[n],reverse=True))
            print(n, end=" ")
    print()

dfs()
bfs()