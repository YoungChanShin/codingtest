# di = [0, -1, 0, 1, -2, -1, 1, 2, -1, 0, 1, 0]
# dj = [-2, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2]
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def check(stage):
    for i in range(5):
        for j in range(5):
            if stage[i][j] == "P":
                if bfs(stage, i, j):
                    return 0  # 위반한 경우
    return 1  # 거리두기 준수


def bfs(stage, i, j):
    visited = []
    q = deque([(i, j, 0)])
    while q:
        i, j, dis = q.pop()
        visited.append((i, j))
        for d in range(4):
            new_i = i + di[d]
            new_j = j + dj[d]
            new_dis = dis + 1
            if (
                -1 < new_i < 5
                and -1 < new_j < 5
                and new_dis < 3
                and (new_i, new_j) not in visited
            ):
                if stage[new_i][new_j] == "P":
                    return True
                if stage[new_i][new_j] == "O":
                    q.append((new_i, new_j, new_dis))
    return False


def solution(places):
    answer = []
    for stage in places:
        answer.append(check(stage))
    return answer


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]

print(solution(places))