def solution(n, k, cmd):
    answer = ""
    data = list(range(n))
    idx = k
    val = k
    dels = []

    for c in cmd:
        command = c[0]
        if command == "U":
            parameter = int(c[2])
            idx = max(0, idx - parameter)
        if command == "D":
            parameter = int(c[2])
            idx = min(len(data) - 1, idx + parameter)

        if command == "C":
            val = data[idx]
            dels.append(val)
            data.pop(idx)
            if idx == len(data) - 1:
                idx -= 1
            #     continue
            # else:
            #     idx += 1

        if command == "Z":
            if len(dels) == 0:
                continue
            val = data[idx]
            recov = dels.pop(-1)
            data.append(recov)
            data.sort()
            if data[idx] != val:
                idx = data.index(val)

    answer = ["X"] * n
    for i in data:
        answer[i] = "O"
    return "".join(answer)


n = 8
k = 2
# cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]  # "OOOOXOOO"
# cmd = ["C", "C", "C", "C", "C", "C", "C", "C"]  # "OOOOXOOO"
# cmd = ["C", "C", "C", "C"]  # "OOOOXOOO"
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]  # "OOXOXOOO"
print(solution(n, k, cmd))