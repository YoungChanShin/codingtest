# https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3


def solution(N, number):

    dp = [{}]
    for i in range(1, 9):
        nth = int(str(N) * i)
        if nth == number:
            return i
        dp.append({nth})
    for i in range(2, 9):  # 숫자를 몇개 쓰나
        for j in range(1, i):  # 앞에 참조하는 숫자 갯수
            for k in dp[j]:  # 계산 결과 중 택 1
                for l in dp[i - j]:
                    result = {k + l, k - l, k * l}
                    if l != 0:
                        result.add(k // l)
                    if number in result:
                        return i
                    dp[i] = dp[i].union(result)
    return -1


print(solution(5, 55))