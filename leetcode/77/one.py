# Return the length of the longest substring containing the same letter
# that you can get after performing the above operations.
from collections import Counter


def solution(s, k) -> int:
    left_idx = 0
    count_letters = Counter()
    for right_idx, letter in enumerate(s, 1):
        count_letters[letter] += 1
        most_commom_iter = count_letters.most_common()[0][1]
        if k >= right_idx - left_idx - most_commom_iter:
            continue
        count_letters[s[left_idx]] -= 1
        left_idx += 1
    return right_idx - left_idx


s = "AABABBA"
k = 1
print(solution(s, k))