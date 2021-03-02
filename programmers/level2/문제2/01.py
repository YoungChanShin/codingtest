def recur(height, start_num, start_line):
    if height == 1:
        return [start_num]
    if height == 2:
        return [] 

def solution(n):
    answer = recur(height=n, start_num=1, start_line=0)
    return answer

print(solution(4))