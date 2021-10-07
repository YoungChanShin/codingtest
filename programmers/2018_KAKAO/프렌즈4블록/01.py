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
    board = [list(dolls) for dolls in board]
    print(board)
    while flag:
        flag = False
        # 삭제할 부분 찾기
        bubble = [[0] * width for _ in range(height)]
        for i in range(height - 1):
            for j in range(width - 1):
                if check(board, i, j):
                    bubble[i][j] = 1
                    bubble[i + 1][j] = 1
                    bubble[i][j + 1] = 1
                    bubble[i + 1][j + 1] = 1
                    flag = True
        for i in range(height):
            for j in range(width):
                if board[i][j] == "0":
                    bubble[i][j] = 1

        # 삭제하고 밀어내기
        new_board = [[0 for i in range(height)] for j in range(width)]
        for i in range(height):
            for j in range(width):
                new_board[j][i] = board[i][j]
        
        new_bubble = [[0 for i in range(height)] for j in range(width)]
        for i in range(height):
            for j in range(width):
                new_bubble[j][i] = bubble[i][j]


        for i in range(width):
            for j in range(height):
                if new_bubble[i][j] == 1:
                    for k in range(j+1,height):
                        if new_bubble[i][k] == 0:
                            new_board[i][j:j+(height-k)] = new_board[i][k:]
                            for l in range(k,height):
                                new_board[i][l]
                            break
                    

        
    return answer


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))
