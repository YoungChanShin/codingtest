'''
현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.

    왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
    왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
    네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
    네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
'''
import sys
sys.stdin = open('input.txt')

# init_i = (0,1,0,-1)
# init_j = (-1,0,1,0)

di = (0,-1,0,1)
dj = (-1,0,1,0)

# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
# 왼쪽: 북 -> 서 -> 남 -> 동
N,M = list(map(int, input().split()))
row, col, direction = list(map(int,input().split()))
if direction == 1:
    direction = 3
elif direction == 3:
    direction = 1

maps = [list(map(int,input().split())) for _ in range(N)]

flag = False
cnt = 0

while True:
    flag = False
    # 1. 해당 칸을 청소하라
    if maps[row][col]==0:
        maps[row][col] = 2
        cnt += 1
    # 2. 청소하지 않은 공간이 존재할 때까지 현재 방향기준 왼쪽 방향부터 차례대로 탐색한다.
    for i in range(4):
        direction += 1
        if direction>3:
            direction -= 4
        # 청소하지 않은 공간을 찾은 경우 그 방향으로 한칸 전진하고 1번부터 진행한다.
        if maps[row+di[direction]][col+dj[direction]] == 0:
            row += di[direction]
            col += dj[direction]
            flag = True
            break
    if flag:
        continue
    # 네 방향이 모두 청소되어 있거나 벽인 경우 바라보는 방향을 유지한 채 한칸 후진한다.
    row -= di[direction]
    col -= dj[direction]
    # if not (-1<row<N and -1<col<M) or maps[row][col] == 1:
    if maps[row][col] == 1:
        break
print(cnt)
