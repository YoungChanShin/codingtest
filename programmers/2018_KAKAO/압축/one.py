def solution(msg):
    answer = []
    dictionary = dict()
    for i in range(65, 65 + 26):
        dictionary[chr(i)] = i - 64
    w = msg[0]
    for idx, l in enumerate(msg[1:]):
        newWord = w + l
        if newWord in dictionary.keys():
            w = newWord
            continue
        else:
            # 등록
            dictionary[newWord] = len(dictionary) + 1
            answer.append(dictionary[w])
            w = l
    answer.append(dictionary[w])

    return answer


msg = "KAKAO"
print(solution(msg))