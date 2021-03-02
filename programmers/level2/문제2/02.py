def solution(n):
    answer = [[0]*n for _ in range(n)]
    answer[0][0] = 1
    def go(start_num, start_line, height):
        for i in range(height):
            answer[start_line+i][start_line//2] = start_num+i
        for i in range(1, height):
            answer[start_line+height-1][start_line//2+i] = start_num+height-1+i
        for i in range(2, height):
            answer[start_line+height-i][start_line//2+height-i] = start_num+2*height+i-3
        return start_num+3*(height-1)

    start_num = 1
    start_line = 0
    height = n

    for i in range(n,0,-3):
        start_num = go(start_num, start_line, i)
        start_line += 2
    ret = []
    for i in range(n):
        ret.extend(answer[i][:(i+1)])
    # return ret
    return answer
for i in solution(6):
    print(i)