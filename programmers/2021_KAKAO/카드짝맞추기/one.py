from itertools import permutations
from collections import defaultdict
import heapq
from copy import deepcopy

# 현재 카드가 놓인 상태를 나타내는 2차원 배열 board와 커서의 처음 위치 r, c가 매개변수로 주어질 때
def solution(board, r, c):
    answer = float('inf')
    # 미리 할일 : 짝의 위치 찾기
    pair = defaultdict(list)
    for row in range(4):
        for col in range(4):
            if board[row][col] != 0:
                pair[board[row][col]].append((row, col))
    
    # 조합 만들기
    for t in list(permutations(pair)):
        c_board = deepcopy(board)
        cnt = 0
        cur_r, cur_c = r, c
        # 반복문 돌기
        for k in t:
            m,cur_r,cur_c = del_card(c_board,cur_r, cur_c,k,pair)
            cnt += m
        if cnt < answer:
            answer = cnt

    return answer

# 해당 지도에서 k를 제거하는데 필요한 최소 움직임수
def del_card(board, r, c, k,pair):
    m = 2 # Enter수는 선반영
    # 현재 위치에서 두개의 카드로 이동하는데 필요한 움직임수
    r1,c1 = pair[k][0]
    r2,c2 = pair[k][1]
    m1,m2 = get_distance(board,r,c,r1,c1)+get_distance(board,r1,c1,r2,c2), get_distance(board,r,c,r2,c2)+get_distance(board,r2,c2,r1,c1)
    if m1 < m2:
        new_r, new_c = r2,c2
        m += m1
    else:
        new_r, new_c = r1,c1
        m += m2
    board[r1][c1] = 0
    board[r2][c2] = 0
    return m,new_r, new_c

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def get_distance(board,r1,c1,r2,c2):
    if r1==r2 and c1==c2:
        return 0
    visited = []
    hq = []
    heapq.heappush(hq,[0,r1,c1])
    while hq:
        d,r,c = heapq.heappop(hq)
        visited.append((r,c))
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if -1< new_r < 4 and -1<new_c<4 and (new_r,new_c) not in visited:
                if new_r == r2 and new_c == c2:
                    return d+1
                heapq.heappush(hq,[d+1,new_r,new_c])
        for i in range(4):
            new_r = r
            new_c = c
            while -1 < new_r + dr[i] < 4 and -1 < new_c + dc[i] < 4:
                new_r += dr[i]
                new_c += dc[i]
                if board[new_r][new_c] != 0:
                    break
            if -1< new_r < 4 and -1<new_c<4 and (new_r,new_c) not in visited:
                if new_r == r2 and new_c == c2:
                    return d+1
                heapq.heappush(hq,[d+1,new_r,new_c])


board =[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r,c = 1,0
print(solution(board, r, c))


# print(get_distance(board, 0,0,3,2)) # 3
# print(get_distance(board, 3,2,0,0)) # 2
# print(get_distance(board, 1,0,2,3)) # 2
# print(get_distance(board, 0,3,3,0)) # 3