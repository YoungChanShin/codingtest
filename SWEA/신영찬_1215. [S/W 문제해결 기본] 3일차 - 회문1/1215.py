def pal(data_string):
    for i in range(len(data_string)//2):
        if data_string[i]!=data_string[-1-i]:
            return False
    return True

for test_case in range(1,11):
    N=int(input())
    data_list=[list(input()) for _ in range(8)]
    ret=0
    for i in range(8):
        if N==1:
            ret=64
            break
        for j in range(9-N):
            if pal(data_list[i][j:j+N]):
                ret+=1
            s=''
            for k in range(N):
                s+=data_list[j+k][i]
            if pal(s):
                ret+=1
    print('#{} {}'.format(test_case,ret))