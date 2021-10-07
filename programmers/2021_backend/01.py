def solution(rows, columns, queries):
    answer = []
    data_list = [[j*columns+i for i in range(1, columns+1)] for j in range(rows)]

    for sr, sc, er, ec in queries:

        temp = data_list[sr-1][sc-1]
        rolls = [temp]

        for r in range(sr,er):
            data_list[r-1][sc-1] = data_list[r][sc-1]
            rolls.append(data_list[r][sc-1])
        
        for c in range(sc, ec):
            data_list[er-1][c-1] = data_list[er-1][c]
            rolls.append(data_list[er-1][c])
        
        for r in range(er-1, sr-1, -1):
            data_list[r][ec-1] = data_list[r-1][ec-1]
            rolls.append(data_list[r-1][ec-1])

        for c in range(ec-1, sc-1, -1):
            data_list[sr-1][c] = data_list[sr-1][c-1]
            rolls.append(data_list[sr-1][c-1])
        
        data_list[sr-1][sc] = temp
        
        answer.append(min(rolls))
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

print(solution(rows, columns, queries))