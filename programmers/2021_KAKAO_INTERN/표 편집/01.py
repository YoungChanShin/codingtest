# 처음 표의 행 개수를 나타내는 정수 n
# 처음에 선택된 행의 위치를 나타내는 정수 k
# 수행한 명령어들이 담긴 문자열 배열 cmd
# cmd의 각 원소는 "U X", "D X", "C", "Z" 중 하나입니다.
# "U X": 현재 선택된 행에서 X칸 위에 있는 행을 선택합니다.
# "D X": 현재 선택된 행에서 X칸 아래에 있는 행을 선택합니다.
# "C" : 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택합니다.
# "Z" : 가장 최근에 삭제된 행을 원래대로 복구합니다. 단, 현재 선택된 행은 바뀌지 않습니다.


def solution(n, k, cmd):
    alive = [0] * n
    cur = k
    deleteds = []

    def up(alive, cur, x):
        for _ in range(x):
            if cur == 0:
                return 0
            cur -= 1
            while alive[cur] == 1:
                cur -= 1
                if cur == 0:
                    return 0
        return cur

    def down(alive, cur, x):
        end = len(alive) - 1
        for _ in range(x):
            if cur == end:
                return end
            cur += 1
            while alive[cur] == 1:
                cur += 1
                if cur == end:
                    return end
        return cur

    for c in cmd:
        if c[0] == "U":
            cur = up(alive, cur, int(c[2]))
        if c[0] == "D":
            cur = down(alive, cur, int(c[2]))
        if c[0] == "C":
            alive[cur] = 1
            deleteds.append(cur)
            cur = down(alive, cur, 1)
            if alive[cur] == 1:
                cur = up(alive, cur, 1)
        if c[0] == "Z":
            alive[deleteds.pop(-1)] = 0

    answer = "".join(["O" if i == 0 else "X" for i in alive])

    return answer


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]

print(solution(n, k, cmd))
