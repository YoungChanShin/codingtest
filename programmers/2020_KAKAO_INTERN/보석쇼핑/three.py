from collections import Counter, defaultdict


def solution(gems):
    data = Counter(gems)
    window = defaultdict(int)
    end, start, left = len(gems) - 1, 0, 0
    numOfTypes = len(data.keys())
    for right, g in enumerate(gems):
        window[g] += 1
        while numOfTypes == len(window.keys()) and left <= right:
            if right - left < end - start:
                start, end = left, right
            window[gems[left]] -= 1
            if window[gems[left]] == 0:
                del window[gems[left]]
            left += 1

    return [start + 1, end + 1]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))