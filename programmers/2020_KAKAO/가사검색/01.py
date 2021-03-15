def solution(words, queries):
    len_queries = len(queries)
    answer = [0] * len_queries
    answer_history = []
    words.sort(key=lambda x:len(x))

    for qi, q in enumerate(queries):
        ql = len(q)
        if q in answer_history:
            for i in range(qi):
                if q == answer_history[i]:
                    answer[qi] = answer[i]
            answer_history.append(q)
            continue
        answer_history.append(q)
        for w in words:
            wl = len(w)
            if wl > ql:
                break
            if wl == ql:
                # compare
                i = 0
                if q[0] == "?":
                    i += 1
                    if q[-1] == "?":
                        # ?가 끝까지 연결되어 있는 상황
                        answer[qi] += 1
                        continue
                    # ?가 접두어로 붙어 있는 경우
                    while i < wl and q[i] == "?":
                        i += 1
                    if w[i:] == q[i:]:
                        answer[qi] += 1
                    continue
                elif w[0] == q[0]:
                    # ?가 접미사로 있는 경우
                    while i < wl and q[i] != "?":
                        i += 1
                    if q[:i] == w[:i]:
                        answer[qi] += 1
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words,queries))