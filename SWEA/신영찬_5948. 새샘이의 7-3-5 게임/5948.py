ts=int(input())
for test_case in range(1,1+ts):
    data_list=sorted(list(map(int,input().split())), reverse=True)
    ret=0
    total=list()
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1,7):
                total.append(data_list[i]+data_list[j]+data_list[k])
    total=sorted(list(set(total)))
    print('#{} {}'.format(test_case,total[-5]))