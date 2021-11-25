ts=int(input())
for test_case in range(1,1+ts):
    data_string=input().strip()
    L=len(data_string)
    how_many_h=int(input())
    location_list=list(map(int,input().split()))
    count_list=[0]*(L+1)
    ret=''
    for i in location_list:
        count_list[i]+=1
    for i in range(L):
        ret+='-'*count_list[i]
        ret+=data_string[i]
    ret+='-'*count_list[-1]
    print('#{} {}'.format(test_case, ret))
'''
strip()을 습관적으로 split()으로 써서 에러가 발생했다.
헛되게 시간을 낭비하지 말자
'''