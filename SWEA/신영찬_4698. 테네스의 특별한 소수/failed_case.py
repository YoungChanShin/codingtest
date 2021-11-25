prime_numbers=[True]*1000001
prime_numbers[0]=False
prime_numbers[1]=False
prime_numbers[4]=False

for i in range(3,500000):
    for j in range(2,2500000):
        if i*j>1000000:
            break
        prime_numbers[i*j]=False
        
ts=int(input())
for test_case in range(1,1+ts):
    D,A,B=list(map(int, input().split()))
    ret=0
    for number in range(A,B+1):
        str_num=str(number)
        for s in str_num:
            if s==str(D):
                if prime_numbers[number]:
                    ret+=1
                    break
    print('#{} {}'.format(test_case,ret))
'''
시간초과함. 시간 초과의 원인은 크게 두군데서 발견됨
1. 소수를 찾을 때 너무 많은 경우를 탐색
2. A와 B사이에 소수가 아닌 경우도 문자열을 변환하고 D와 매칭하고 난 후에 소수임을 확인하는 로직이 있음
'''
