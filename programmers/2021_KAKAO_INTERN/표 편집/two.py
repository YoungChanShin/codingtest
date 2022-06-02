def solution(n, k, cmd):
    data_dict = {i: [i - 1, i + 1] for i in range(-1, n + 1)}
    # data_dict[0][0] = 0
    # data_dict[n - 1][1] = n - 1
    dels = []
    for c in cmd:
        d = c.split()[0]
        if d == "U":
            for _ in range(int(c.split()[1])):
                k = data_dict[k][0]

        if d == "D":
            for _ in range(int(c.split()[1])):
                k = data_dict[k][1]

        if d == "C":
            prevNode = data_dict[k][0]
            nextNode = data_dict[k][1]

            data_dict[prevNode][1] = nextNode
            data_dict[nextNode][0] = prevNode

            dels.append([k, data_dict[k]])
            if nextNode == n:
                k = prevNode
            else:
                k = nextNode

        if d == "Z":
            zPos, zVal = dels.pop()
            prevNode, nextNode = zVal
            data_dict[prevNode][1] = zPos
            data_dict[nextNode][0] = zPos

    answer = ["X" for _ in range(n)]
    s = data_dict[-1][1]
    while s != n:
        answer[s] = "O"
        s = data_dict[s][1]

    return "".join(answer)


n = 8
k = 2
# cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]  # "OOOOXOOO"
# cmd = ["C", "C", "C", "C", "C", "C", "C", "C"]  # "OOOOXOOO"
# cmd = ["C", "C", "C", "C"]  # "OOOOXOOO"
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]  # "OOXOXOOO"
print(solution(n, k, cmd))
