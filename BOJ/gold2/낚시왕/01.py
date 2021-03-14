import sys
sys.stdin = open('input.txt')

R,C,M = list(map(int,input().split()))
maps = [[[]]*C for _ in range(R)]

# 상어의 정보는 다섯 정수 r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 이루어져 있다. 
# (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. 
# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.

for _ in range(M):
    r, c, s, d, z = list(map(int,input().split()))
    maps[r-1][c-1] = [s,d,z]

def move(maps, r, c):
    # r,c에 있는 상어가 움직이고 나서 결과 위치를 반환
    s, d, z = maps[r][c]
    if d == 1:
        r -= s
        while r<0 or len(maps)<=r:
            if r < 0:
                r = -r
                d = 2
            if len(maps) <= r:
                r = 2*len(maps)-r-2
                d = 1
    elif d == 2:
        r += s
        while r<0 or len(maps)<=r:
            if r < 0:
                r = -r
                d = 2
            if len(maps) <= r:
                r = 2*len(maps)-r-2
                d = 1
    elif d == 3:
        c += s
        while c<0 or len(maps[0])<=c:
            if c < 0:
                c = -c
                d = 3
            if len(maps[0])<=c:
                c = 2*len(maps[0])-c-2
                d = 4
    elif d == 4:
        c -= s
        while c<0 or len(maps[0])<=c:
            if c < 0:
                c = -c
                d = 3
            if len(maps[0])<=c:
                c = 2*len(maps[0])-c-2
                d = 4
    return r,c,d

cnt = 0
for i in range(C):
    # # 출력
    # for x in maps:
    #     print(x)
    # 낚시
    for j in range(R):
        if maps[j][i]:
            cnt += maps[j][i][2]
            maps[j][i] = []
            break
    
    # 상어 이동
    new_s = []
    for si in range(R):
        for sj in range(C):
            if maps[si][sj]:
                ni,nj,nd = move(maps, si, sj)
                new_s.append((ni,nj,maps[si][sj][0],nd,maps[si][sj][2]))

    for i in range(R):
        for j in range(C):
            maps[i][j] = []
    for shark in new_s:
        r, c, s, d, z = shark
        if maps[r][c]: 
            if maps[r][c][2] < z:
                maps[r][c] = (shark[2],shark[3],shark[4])
        else:
            maps[r][c] = (shark[2],shark[3],shark[4])
print(cnt)