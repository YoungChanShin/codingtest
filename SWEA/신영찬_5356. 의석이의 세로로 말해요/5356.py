ts=int(input())
for test_case in range(1,1+ts):
    data_list=list()
    max_len=0
    for _ in range(5):
        data=input().strip()
        data_list.append(data)
        cnt=len(data)
        if max_len<cnt:
            max_len=cnt
    for i in range(5):
        data_list[i]+=(' '*(max_len-len(data_list[i])))
    print('#{} '.format(test_case), end='')
    for i in range(max_len):
        for j in range(5):
            if data_list[j][i]!=' ':
                print(data_list[j][i], end='')
    print()