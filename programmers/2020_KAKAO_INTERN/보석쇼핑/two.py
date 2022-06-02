from collections import Counter


def solution(gems):
    t_counter = Counter(gems)
    t_counter_key = t_counter.keys()
    window = dict()

    def check():
        for k in t_counter_key:
            if window[k] < 1:
                return False
        return True

    for k in t_counter_key:
        window[k] = 0
    left = 0
    for right in range(len(gems)):
        g = gems[right]
        window[g] += 1
        if check():
            right_start = right
            break
    start, end = 0, right_start

    for right in range(right_start, len(gems)):
        g = gems[right]
        window[g] += 1
        while window[gems[left]] > 1 and left < right:
            window[gems[left]] -= 1
            left += 1
            if end - start > right - left:
                end, start = right, left

    return [start + 1, end + 1]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems = ["XYZ", "XYZ", "XYZ"]
gems = ["AAA", "YYY", "NNNN", "AAA", "AAA"]

print(solution(gems))