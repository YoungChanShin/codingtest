def isCollect(p):
    cnt = 0
    for i in p:
        if i == "(":
            cnt += 1
        if i == ")":
            cnt -= 1
        if cnt < 0:
            return False
    if cnt == 0:
        return True
    return False


def solution(p):
    if isCollect(p):
        return p
    answer = ""
    cnt = 0
    for idx, letter in enumerate(p):
        if letter == "(":
            cnt += 1
        if letter == ")":
            cnt -= 1
        if cnt == 0:
            if isCollect(p[: idx + 1]):
                return p[: idx + 1] + solution(p[idx + 1 :])
            else:
                temp = ""
                for ul in p[1:idx]:
                    if ul == "(":
                        temp += ")"
                    if ul == ")":
                        temp += "("
                return "(" + solution(p[idx + 1 :]) + ")" + temp
            answer = solution(p[: idx + 1]) + solution(p[idx + 1 :])
    return answer