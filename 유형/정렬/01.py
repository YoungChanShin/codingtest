def solution(array, commands):
    answer = []
    for c in commands:
        segment = sorted(array[c[0] - 1 : c[1]])
        answer.append(segment[c[2] - 1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
command = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, command))