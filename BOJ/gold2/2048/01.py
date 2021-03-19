import sys
sys.stdin = open('input.txt')

from copy import deepcopy

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

directions = (0,1,2,3) # 0은 왼쪽, 1은 오른쪽, 2는 위, 3은 아래
max_val = 0

def move(board, d):
    new_board = deepcopy(board)
    # 0은 왼쪽(<-), 1은 오른쪽(->), 2는 위(^), 3은 아래(V)
    if d == 0:
        for i in range(N):
            # recent_idx는 밀었을 때 들어갈 수 있는 위치
            recent_idx = 0

            for j in range(1,N):
                # 해당 칸에 블럭이 있고 최근 index 칸과 값이 같은 경우 합치기
                if new_board[i][j] != 0:

                    # recent_idx의 블럭값이 0일 때
                    if new_board[i][recent_idx] == 0:
                        new_board[i][recent_idx] = new_board[i][j]
                        new_board[i][j] = 0
                        continue

                    # recent_idx의 블럭값이 0이 아니고 j의 블럭값이 같을 때
                    if new_board[i][recent_idx] == new_board[i][j]:
                        new_board[i][recent_idx] *= 2
                        new_board[i][j] = 0
                        recent_idx += 1
                        continue

                    # recent_idx의 블럭값이 0이 아니고 j의 블럭값과 다를 때 ==> 
                    else:
                        recent_idx += 1
                        temp = new_board[i][j]
                        new_board[i][j] = 0
                        new_board[i][recent_idx] = temp

    if d == 1:
        for i in range(N):
            # recent_idx는 밀었을 때 들어갈 수 있는 위치
            recent_idx = N-1

            for j in range(N-2, -1, -1):
                # 해당 칸에 블럭이 있고 최근 index 칸과 값이 같은 경우 합치기
                if new_board[i][j] != 0:

                    # recent_idx의 블럭값이 0일 때
                    if new_board[i][recent_idx] == 0:
                        new_board[i][recent_idx] = new_board[i][j]
                        new_board[i][j] = 0
                        continue

                    # recent_idx의 블럭값이 0이 아니고 j의 블럭값이 같을 때
                    if new_board[i][recent_idx] == new_board[i][j]:
                        new_board[i][recent_idx] *= 2
                        new_board[i][j] = 0
                        recent_idx -= 1
                        continue

                    # recent_idx의 블럭값이 0이 아니고 j의 블럭값과 다를 때 ==> 
                    else:
                        recent_idx -= 1
                        temp = new_board[i][j]
                        new_board[i][j] = 0
                        new_board[i][recent_idx] = temp
    if d == 2:
        for i in range(N):
            # recent_idx는 밀었을 때 들어갈 수 있는 위치
            recent_idx = 0

            for j in range(1,N):
                # 해당 칸에 블럭이 있고 최근 index 칸과 값이 같은 경우 합치기
                if new_board[j][i] != 0:

                    # recent_idx의 블럭값이 0일 때
                    if new_board[recent_idx][i] == 0:
                        new_board[recent_idx][i] = new_board[j][i]
                        new_board[j][i] = 0
                        continue

                    # recent_idx의 블럭값이 0이 아니고 j의 블럭값이 같을 때
                    if new_board[recent_idx][i] == new_board[j][i]:
                        new_board[recent_idx][i] *= 2
                        new_board[j][i] = 0
                        recent_idx += 1
                        continue

                    # recent_idx의 블럭값이 0이 아니고 j의 블럭값과 다를 때 ==> 
                    else:
                        recent_idx += 1
                        temp = new_board[j][i]
                        new_board[j][i] = 0
                        new_board[recent_idx][i] = temp
    if d == 3:
        for i in range(N):
            # recent_idx는 밀었을 때 들어갈 수 있는 위치
            recent_idx = N-1

            for j in range(N-2,-1,-1):
                # 해당 칸에 블럭이 있고 최근 index 칸과 값이 같은 경우 합치기
                if new_board[j][i] != 0:

                    # recent_idx의 블럭값이 0일 때
                    if new_board[recent_idx][i] == 0:
                        new_board[recent_idx][i] = new_board[j][i]
                        new_board[j][i] = 0
                        continue

                    # recent_idx의 블럭값이 0이 아니고 j의 블럭값이 같을 때
                    if new_board[recent_idx][i] == new_board[j][i]:
                        new_board[recent_idx][i] *= 2
                        new_board[j][i] = 0
                        recent_idx -= 1
                        continue

                    # recent_idx의 블럭값이 0이 아니고 j의 블럭값과 다를 때 ==> 
                    else:
                        recent_idx -= 1
                        temp = new_board[j][i]
                        new_board[j][i] = 0
                        new_board[recent_idx][i] = temp
    
    return new_board
                        

for i1 in directions:
    first_board = move(board, i1)

    for i2 in directions:
        second_board = move(first_board, i2)

        for i3 in directions:
            third_board = move(second_board, i3)

            for i4 in directions:
                fourth_board = move(third_board, i4)

                for i5 in directions:
                    fifth_board = move(fourth_board, i5)

                    for r in range(N):
                        for c in range(N):
                            max_val = max(max_val, fifth_board[r][c])

print(max_val)