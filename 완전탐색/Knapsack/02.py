def sol(k,n):
    a = [[0 for _ in range(k+2)]for _ in range(n+2)]
    for i in range(1,n+1):
        for j in range(1,k+1):
            if v_list[i-1] > j:
                a[i][j] = a[i-1][j]
            else:
                a[i][j] = max(c_list[i-1]+a[i-1][j-v_list[i-1]], a[i-1][j])
    return a[n][k]

for t in range(int(input())):
    N, K = map(int, input().split())
    sack = [list(map(int, input().split()))for _ in range(N)]
    v_list = []
    c_list = []
    for i in range(N):
        v_list.append(sack[i][0])
        c_list.append(sack[i][1])
    print(f"#{t+1} {sol(K,N)}")