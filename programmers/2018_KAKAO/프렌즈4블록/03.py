def check(board, i, j):
    cond = board[i][j]
    return (
        cond != "0"
        and board[i + 1][j] == cond
        and board[i][j + 1] == cond
        and board[i + 1][j + 1] == cond
    )


def solution(height, width, board):
    answer = 0
    flag = True
    board = [l[::-1] for l in list(map(list, zip(*board)))]
    while flag:
        pq = set()
        flag = False
        for i in range(width - 1):
            for j in range(height - 1):
                if check(board, i, j):
                    flag = True
                    pq.add((i, j))
                    pq.add((i, j + 1))
                    pq.add((i + 1, j))
                    pq.add((i + 1, j + 1))

        pq_s = sorted(list(pq), reverse=True)
        # 삭제하기
        for row, col in pq_s:
            del board[row][col]
            board[row].append("0")
            answer += 1
    return answer


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))
