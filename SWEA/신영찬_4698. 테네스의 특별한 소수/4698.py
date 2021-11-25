prime_numbers=[True]*1000001
prime_numbers[0]=False
prime_numbers[1]=False
prime_numbers[4]=False
flag=False
for i in range(3,500000):
    for j in range(2,333334):
        if i*j>1000000:
            break
        prime_numbers[i*j]=False
        
ts=int(input())
for test_case in range(1,1+ts):
    D,A,B=list(map(int, input().split()))
    ret=0
    for number in range(A,B+1):
        if prime_numbers[number]:
            str_num=str(number)
            for s in str_num:
                if s==str(D):
                    ret+=1
                    break
    print('#{} {}'.format(test_case,ret))