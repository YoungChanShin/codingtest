from collections import Counter


def solution(gems):
    g_counter = Counter(gems)
    left, right = 0, len(gems) - 1
    while g_counter[gems[right]] > 1:
        g_counter[gems[right]] -= 1
        right -= 1

    while g_counter[gems[left]] > 1:
        g_counter[gems[left]] -= 1
        left += 1

    return [left + 1, right + 1]


gems = [
    "RUBY",
    "RUBY",
    "EMERALD",
    "SAPPHIRE",
    "DIA",
    "DIA",
    "RUBY",
    "RUBY",
    "DIA",
    "DIA",
    "EMERALD",
    "SAPPHIRE",
    "DIA",
]

print(solution(gems))