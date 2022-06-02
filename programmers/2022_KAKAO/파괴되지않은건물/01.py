def isContain(cur_x, cur_y, turn):
    ty, r1, c1, r2, c2, degr = turn
    if r1 <= cur_y <= r2 and c1 <= cur_x <= c2:
        return True
    return False


def solution(board, skill):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            gage = board[i][j]
            for k in skill:
                if isContain(j, i, k):
                    if k[0] == 1:
                        gage -= k[5]
                    else:
                        gage += k[5]
            if gage > 0:
                answer += 1

    return answer


board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
print(solution(board, skill))