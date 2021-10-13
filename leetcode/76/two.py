from collections import Counter


def solution(s, t) -> str:
    left_idx = 0
    start_idx = 0
    end_idx = 0

    needs = Counter(t)  # 필요한 문자 목록
    missings = len(t)  # 필요한 문자 갯수
    for right_idx, right_letter in enumerate(s):
        # 필요한 문자가 다 나올 때까지 윈도우 확장
        if right_letter in needs.keys():
            needs[right_letter] -= 1
            if needs[right_letter] >= 0:
                missings -= 1

        # 필요없는 것이 있으면 줄이는 축소
        while missings == 0 and (
            s[left_idx] not in needs.keys() or needs[s[left_idx]] < 0
        ):
            if s[left_idx] in needs.keys():
                needs[s[left_idx]] += 1
            left_idx += 1
        if right_idx - left_idx < end_idx - start_idx:
            end_idx, start_idx = right_idx, left_idx

    if start_idx == end_idx:
        return ""
    return s[start_idx : end_idx + 1]


s = "ADOBECODEBANC"
t = "ABC"
print(solution(s, t))
