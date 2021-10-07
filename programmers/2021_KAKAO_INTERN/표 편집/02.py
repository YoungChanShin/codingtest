# from collections import deque


def solution(n, k, cmd):

    alive = list(range(n))
    deleteds = []
    pointer = [k, k]  # index, data
    records = []

    def up(cur, x):
        return max(cur - x, 0)

    def down(cur, x):
        end = len(alive) - 1
        return min(cur + x, end)

    def getIdx(data):
        if data > -1:
            return alive.index(data)
        print(alive)
        return 0

    def getData(idx):
        if len(alive):
            return alive[idx]
        return -1

    def printResult():
        answer = ["X"] * n
        for i in alive:
            answer[i] = "O"
        print("".join(answer))
        print()

    for c in cmd:
        index, data = pointer

        if c[0] == "U":
            index = up(index, int(c[2]))
        if c[0] == "D":
            index = down(index, int(c[2]))
        if c[0] == "C":
            records.append(alive[:])
            data = getData(index)
            alive.remove(data)
            index = min(index, len(alive) - 1)

        if c[0] == "Z":
            data = getData(index)
            alive = records.pop(-1)
            # print(alive)
            index = getIdx(data)

        pointer = [index, data]
        # print(records)
        # printResult()

    answer = ["X"] * n
    for i in alive:
        answer[i] = "O"
    return "".join(answer)


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]  # "OOOOXOOO"
# cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]  # "OOXOXOOO"

n = 5
k = 4
cmd = ["U 2", "D 2", "C", "C", "C", "C", "C", "Z"]
print(solution(n, k, cmd))