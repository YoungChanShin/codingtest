import sys
sys.stdin = open('input.txt')

inf = float('inf')

def dijkstra(adj, start):
    V = len(adj)
    dist = [inf]*V
    visited = [0]*V
    dist[start] = 1

    while True:
        closest = inf
        here = inf
        for i in range(V):
            if dist[i] < closest and not visited[i]:
                here = i
                closest = dist[i]
        if closest == inf:
            break
        visited[here] = 1
        size = len(adj[here])
        for i in range(size):
            there = adj[here][i][0]
            if visited[there]:
                continue
            nextDist = dist[here] * adj[here][i][1]
            dist[there] = min(dist[there], nextDist)
    
    return dist



for i in range(int(input())):
    V, E = list(map(int,input().split()))
    adj = [[] for _ in range(V)]
    for _ in range(E):
        s, e, cost = input().split()
        s = int(s)
        e = int(e)
        cost = float(cost)
        adj[s].append([e,cost])
        adj[e].append([s,cost])
    ret = dijkstra(adj, 0)
    print(ret[-1])
