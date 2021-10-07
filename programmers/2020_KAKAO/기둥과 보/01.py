def validate(maps, y,_x):
    # 기둥
    if _x%2:
        # 바닥위
        if y==0:
            return True
        # 보 한쪽 끝:
        if _x == 0 and maps[y][_x+1]:
            return True
        if _x == len(maps[0])-1 and maps[y][_x-1]:
            return True
        if 0<_x<len(maps[0])-1 and maps[y][_x+1] or maps[y][_x-1]:
            return True
        # 다른 기둥 위
        if maps[y-1][_x]:
            return True
    # 보
    else:
        # 한쪽 끝이 기둥 위
        if maps[y-1][_x+1] or maps[y-1][_x-1]:
            return True
        # 양쪽이 다른 보와 연결
        if 1<_x<len(maps[0])-2 maps[y][_x-2] and maps[y][_x+2]:
            return True
    return False


def solution(n, build_frame):
    answer = []
    maps = [[0]*(2*n+1) for _ in range(n+1)]
    for frame in build_frame:
        # 기둥과 보가 구분없이 사용가능한 좌표계로 변환
        x, y, a, b = frame
        _x = 2*x + a
        # 설치
        if b == 1:
            # 기둥 1. 바닥이면 설치 가능
            if a == 0:
                if y == 0:
                    maps[y][_x] = 1
                    continue
            # 기둥 2. 보 한쪽 위에 설치 가능
                if _x+1<2*n+1 and 0<_x:
                    if maps[y][_x-1] and not maps[y][_x+1]:
                        maps[y][_x] = 1
                        continue
                    if maps[y][_x-1] and not maps[y][_x+1]:
                        maps[y][_x] = 1
                        continue
                if _x == 0:
                    if maps[y][1]:
                        maps[y][_x] = 1
                        continue
                if _x == 2*n:
                    if maps[y][_x-1]:
                        maps[y][_x]
                        continue
            # 기둥 3. 기둥 바로 위에 설치 가능
                if maps[y-1][_x]:
                    maps[y][_x] = 1
                    continue

            if a == 1:
            # 보 1. 설치할 보의 한쪽 끝에 기둥
                if maps[y-1][_x+1] or maps[y-1][_x-1]:
                    maps[y][_x] = 1
                    continue

            # 보 2. 양쪽에 보가 있는 경우
                if 1<_x<2*n-1:
                    if maps[y][_x-2] and maps[y][_x+2]:
                        maps[y][_x] = 1
                        continue

        # 삭제
        if b == 0:
            # 기둥
            if a == 1:
                # 위에 있는 기둥, 좌, 우
                if (y<n-1 and validate(maps,y+1,_x)) and:
                if maps[y+1][_x]:
                    if maps[y]

            pass

    for i in range(n+1):
        for j in range(2*n+1):
            if maps[i][j]:
                if j%2:
                    # 보
                    answer.append([j//2,i,1])
                else:
                    # 기둥
                    answer.append([j//2,i,0])
    answer.sort(key=lambda x: (x[0],x[1],-x[2]))
    return answer

n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))