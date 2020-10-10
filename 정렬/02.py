def solution(numbers):
    answer = ""
    str_nums = sorted(list(map(lambda x: str(x), numbers)), reverse=True)
    return str_nums


numbers = [3, 9, 34, 5, 30]

print(solution(numbers))