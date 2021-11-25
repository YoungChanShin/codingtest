data = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
]


def compress(s, chunk):
    s_len = len(s)
    ch_len = len(chunk)
    iteration = s_len // ch_len
    for i in range(iteration):
        if chunk != s[i * ch_len : (i + 1) * ch_len]:
            return i
    return iteration


def solution(s):
    answer = len(s)
    s_len = answer
    half_s_len = s_len // 2
    for i in range(1, half_s_len + 1):
        num_of_starting_point = s_len // i
        j = 0
        result = ""
        while j < num_of_starting_point:
            chunk = s[j * i : j * i + i]
            iteration = compress(s[j * i :], chunk)
            j += iteration
            if iteration > 1:
                result += str(iteration) + chunk
            else:
                result += chunk
        result += s[num_of_starting_point * i :]
        answer = min(answer, len(result))

    return answer


for d in data:
    print(solution(d))