ts=int(input())
        
def dfs(graph, N):
    count=0
    for start_v in range(N):
        #tri_list=[start_v]
        first_demension=[i for i in range(start_v, N) if graph[start_v][i]]
        for j in first_demension:
            #tri_list.append(j)
            second_demension=[i for i in range(j, N) if graph[j][i]]
            for k in second_demension:
                third_demension=[i for i in range(N) if graph[k][i]]
                if start_v in third_demension:
                    count+=1
    return count

for test_case in range(1,1+ts):
    N,M=list(map(int, input().split()))
    graph=[[False]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        start_v, end_v= list(map(int,input().split()))
        graph[start_v][end_v]=True
        graph[end_v][start_v]=True
    print('#{} {}'.format(test_case, dfs(graph, N+1)))