def solution(n, k, cmd):
    alive = [0] * n
    cur = k
    deleteds = []

    def up(alive, cur, x):
        for _ in range(x):
            cur -= 1
            while cur > 0 and alive[cur] == 1:
                cur -= 1
        return max(0, cur)

    def down(alive, cur, x):
        end = len(alive) - 1
        for _ in range(x):
            cur += 1
            while cur < end and alive[cur] == 1:
                cur += 1
        return min(cur, end)

    for c in cmd:
        if c[0] == "U":
            cur = up(alive, cur, int(c[1:].strip()))
        if c[0] == "D":
            cur = down(alive, cur, int(c[1:].strip()))
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