month_day=[31,29,31,30,31,30,31,31,30,31,30,31]
def convert_date_to_number(m,d):
    ret=0
    for i in range(m-1):
        ret+=month_day[i]
    ret+=d
    ret+=3
    ret%=7
    return ret
ts=int(input())
for test_case in range(1,1+ts):
    m,d=list(map(int,input().split()))
    ret=convert_date_to_number(m,d)
    print("#{} {}".format(test_case, ret))