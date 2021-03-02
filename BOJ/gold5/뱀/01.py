import sys
sys.stdin = open('input.txt')
from collections import deque

# 0: 동, 1:북, 2:서, 3:남
di = (0,-1,0,1)
dj = (1,0,-1,0)
direction = 0

N = int(input())
board = [[0]*(N+1) for _ in range(N+1)]

for _ in range(int(input())):
    i, j = list(map(int,input().split()))
    board[i][j] = 2

commands = deque()
for _ in range(int(input())):
    commands.append(input().split())

time = 0
head = [1,1]
body = deque()
body.append([1,1])

while True:
    # head 이동
    new_head = [0,0]
    new_head[0] = head[0] + di[direction]
    new_head[1] = head[1] + dj[direction]
    time += 1

    # 벽이나 몸이 있으면 종료
    if new_head[0] < 1 or N < new_head[0] or new_head[1] < 1 or N < new_head[1] or new_head in body:
        break

    # command 시간을 확인해서 시간이 일치하면 방향전환
    if commands and int(commands[0][0]) == time:
        if commands[0][1] == 'L':
            direction = (direction+1)%4
        else:
            direction = (direction+3)%4
        commands.popleft()

    # head 이동 후 사과 있으면 while문 처음으로
    head = new_head
    body.append(new_head)
    if board[new_head[0]][new_head[1]] == 2:
        board[new_head[0]][new_head[1]] = 0
        continue

    # 사과 없으면 꼬리를 제거 
    body.popleft()

print(time)

