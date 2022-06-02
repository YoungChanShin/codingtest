# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p
def alter(n, q):
    if n == 0:
        return "0"
    rev_base = ""

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += (
            str(mod)
            .replace("10", "A")
            .replace("11", "B")
            .replace("12", "C")
            .replace("13", "D")
            .replace("14", "E")
            .replace("15", "F")
        )

    return rev_base[::-1]


def solution(n, t, m, p):
    whole = ""
    for i in range(26500):
        whole += alter(i, n)

    print(len(whole))
    answer = "".join(whole[p - 1 : m * t : m])
    return answer


print("13579BDF01234567" == solution(16, 16, 2, 2))
