# skill의 각 행은 [type, r1, c1, r2, c2, degree]형태를 가지고 있습니다.


def solution(board, skill):
    answer = 0
    cumulative_sum = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for turn in skill:
        ty, r1, c1, r2, c2, degree = turn
        if ty == 1:
            degree = -degree
        r2 += 1
        c2 += 1
        cumulative_sum[r1][c1] += degree
        cumulative_sum[r1][c2] -= degree
        cumulative_sum[r2][c1] -= degree
        cumulative_sum[r2][c2] += degree

    for r in range(1, len(board) + 1):
        for c in range(len(board[0]) + 1):
            cumulative_sum[r][c] += cumulative_sum[r - 1][c]

    for r in range(len(board) + 1):
        for c in range(1, len(board[0]) + 1):
            cumulative_sum[r][c] += cumulative_sum[r][c - 1]

    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += cumulative_sum[r][c]
            if board[r][c] > 0:
                answer += 1

    return answer


board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
print(solution(board, skill))