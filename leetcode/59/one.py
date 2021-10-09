def merge(intervals):
    def eclipse(inter1, inter2):
        if inter1[0] > inter2[0]:
            inter1, inter2 = inter2, inter1
        return inter1[1] >= inter2[0]

    intervals.sort(key=lambda x: x[0])
    ret = [intervals[0]]
    for idx in range(1, len(intervals)):
        if eclipse(ret[-1], intervals[idx]):
            ret[-1] = [ret[-1][0], max(ret[-1][1], intervals[idx][1])]
        else:
            ret.append(intervals[idx])
    return ret


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))