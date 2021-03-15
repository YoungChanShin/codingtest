import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,M,H = list(map(int,input().split()))

pick = [[0]*(N+1) for _ in range(H+1)]
for i in range(M):
    i,j = list(map(int,input().split()))
    pick[i][j] = 1
candidates = []

for i in range(1,H+1):
    for j in range(1,N):
        if pick[i][j]==0 and pick[i][j-1]==0 and pick[i][j+1]==0:
            candidates.append([i,j])

def simulate():
    for i in range(1,N+1):
        sj = i
        for j in range(1,H+1):
            if pick[j][sj]:
                sj += 1
            elif pick[j][sj-1]:
                sj -= 1
        if sj == i:
            continue
        else:
            return False
    return True

def solution():
    # 0개 선택
    if simulate():
        return 0
    # 1개 선택
    for i in range(len(candidates)):
        i1,i2 = candidates[i]
        pick[i1][i2] = 1
        if simulate():
            return 1
        pick[i1][i2] = 0

    # 2개 선택
    for i in range(len(candidates)-1):
        i1,i2 = candidates[i]
        pick[i1][i2] = 1
        for j in range(i+1, len(candidates)):
            j1,j2 = candidates[j]
            pick[j1][j2] = 1
            if simulate():
                return 2
            pick[j1][j2] = 0
        pick[i1][i2] = 0

    # 3개 선택
    for i in range(len(candidates)-2):
        i1,i2 = candidates[i]
        pick[i1][i2] = 1
        for j in range(i+1, len(candidates)-1):
            j1,j2 = candidates[j]
            pick[j1][j2] = 1
            for k in range(j+1, len(candidates)):
                k1,k2 = candidates[k]
                pick[k1][k2] = 1
                if simulate():
                    return 3
                pick[k1][k2] = 0
            pick[j1][j2] = 0
        pick[i1][i2] =0

    return -1

print(solution())