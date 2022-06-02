def solution(s):
    answer = len(s)
    cnt = 1

    for l in range(1, len(s) // 2 + 1):
        strLen = l
        unit = s[:l]
        for idx in range(l, len(s) + 1, l):
            if s[idx : idx + l] == unit:
                cnt += 1
            else:
                if cnt > 1:
                    strLen += len(str(cnt))
                cnt = 1
                unit = s[idx : idx + l]
                strLen += len(unit)

        # if cnt > 1:
        #     strLen += len(str(cnt))
        if strLen < answer:
            answer = strLen

    return answer


# ss = [
#     "aabbaccc",
#     "ababcdcdababcdcd",
#     "abcabcdede",
#     "abcabcabcabcdededededede",
#     "xababcdcdababcdcd",
#     "a",
# ]
# for s in ss:
#     print(solution(s))

s = "abc" * 10
s += "def" * 10
print(solution(s))