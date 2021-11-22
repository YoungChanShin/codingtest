import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


answer = 0
R, C, T = list(map(int, input().split()))
data_list = [list(map(int, input().split())) for _ in range(R)]


def getPurifier():
    for i in range(R):
        if data_list[i][0] == -1:
            return i


purifier = getPurifier()


def disperse():
    global data_list, R, C, purifier
    new_date_list = [[0] * C for _ in range(R)]
    new_date_list[purifier][0] = -1
    new_date_list[purifier + 1][0] = -1

    def disperse_one(row, col):
        new_date_list[row][col] += data_list[row][col]
        cnt = 0
        unit = data_list[row][col] // 5
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if (-1 < nr < R and -1 < nc < C) and (
                nc != 0 or (nr not in (purifier, purifier + 1))
            ):
                new_date_list[nr][nc] += unit
                cnt += 1
        new_date_list[row][col] -= cnt * unit
        return

    for row in range(R):
        for col in range(C):
            if data_list[row][col] > 0:
                disperse_one(row, col)
    data_list = new_date_list
    return


def rotate():
    global data_list, R, C, purifier
    # 위
    for i in range(purifier - 1, 0, -1):
        data_list[i][0] = data_list[i - 1][0]
    for i in range(C - 1):
        data_list[0][i] = data_list[0][i + 1]
    for i in range(purifier):
        data_list[i][C - 1] = data_list[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        data_list[purifier][i] = data_list[purifier][i - 1]
    data_list[purifier][1] = 0

    # 아래
    for i in range(purifier + 2, R - 1):
        data_list[i][0] = data_list[i + 1][0]
    for i in range(C - 1):
        data_list[R - 1][i] = data_list[R - 1][i + 1]
    for i in range(R - 1, purifier + 1, -1):
        data_list[i][C - 1] = data_list[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        data_list[purifier + 1][i] = data_list[purifier + 1][i - 1]
    data_list[purifier + 1][1] = 0

    return


for _ in range(T):
    disperse()
    rotate()

for i in data_list:
    answer += sum(i)

print(answer + 2)
