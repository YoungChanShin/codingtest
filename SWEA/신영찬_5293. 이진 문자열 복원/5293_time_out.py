def bin_tree(ret, A, B, C, D):
    #초기화
    if ret=='':
        ret=bin_tree('0', A, B, C, D)
        if ret=='impossible':
            return bin_tree('1', A, B, C, D)
        return ret
    # 종료조건
    if A + B == 0 and C + D != 0 and ret[-1] == '0':
        return 'impossible'
    if C + D == 0 and A + B != 0 and ret[-1] == '1':
        return 'impossible'
    if A + B + C + D == 0:
        return ret

    if ret[-1] == '0' and A>0:
        ret1 = ret + '0'
        tree_00 = bin_tree(ret1, A - 1, B, C, D)
        if tree_00 != 'impossible':
            return tree_00
    if ret[-1] == '0' and B>0:
        ret2 = ret + '1'
        tree_01 = bin_tree(ret2, A, B - 1, C, D)
        if tree_01 != 'impossible':
            return tree_01

    if ret[-1] == '1' and C>0:
        ret3 = ret + '0'
        tree_10 = bin_tree(ret3, A, B, C - 1, D)
        if tree_10 != 'impossible':
            return tree_10
    if ret[-1] == '1' and D>0:
        ret4 = ret + '1'
        tree_11 = bin_tree(ret4, A, B, C, D - 1)
        if tree_11 != 'impossible':
            return tree_11
    return 'impossible'


ts = int(input())
for test_case in range(1, 1 + ts):
    A, B, C, D = list(map(int, input().split()))
    result=bin_tree('', A, B, C, D)
    print('#{} {}'.format(test_case,result))