words = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solution(s):
    answer = ""
    idx = 0
    word = ""
    while idx < len(s):
        if s[idx].isdigit():
            answer += s[idx]
        else:
            word += s[idx]
            if word in words.keys():
                answer += str(words[word])
                word = ""
        idx += 1
    return int(answer)
