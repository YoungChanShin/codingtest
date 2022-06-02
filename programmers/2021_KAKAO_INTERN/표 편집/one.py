def solution(n, k, cmd):
    pos = k
    dels = []
    data_list = list(range(n))
    for c in cmd:
        d = c.split()[0]
        if d == "U":
            x = int(c.split()[1])
            pos = pos - x
        if d == "D":
            x = int(c.split()[1])
            pos = pos + x

        if d == "C":
            dels.append([pos, data_list[pos]])
            data_list.pop(pos)
            pos = min(pos, len(data_list) - 1)

        elif d == "Z":
            zPos, zVal = dels.pop()
            if zPos <= pos:
                pos += 1
            data_list.insert(zPos, zVal)

    answer = ["X" for _ in range(n)]
    for i in data_list:
        answer[i] = "O"
    return "".join(answer)


n = 8
k = 2
# cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]  # "OOOOXOOO"
# cmd = ["C", "C", "C", "C", "C", "C", "C", "C"]  # "OOOOXOOO"
# cmd = ["C", "C", "C", "C"]  # "OOOOXOOO"
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]  # "OOXOXOOO"
print(solution(n, k, cmd))