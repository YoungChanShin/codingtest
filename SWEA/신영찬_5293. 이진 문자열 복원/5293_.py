'''
내가 발견한 원칙은 다음과 같다
1. 결과값은 A+B+C+D+1자리 수이다.
2. 불가능
    B=C=0인데 A와 D둘다 0이 아니다.
    C와 D의 차이가 2 이상이다.
3. 불가능을 제외하면
    a와 d가 0인 경우에 예외 처리를 해주고나서
        b-c값에 따라 문자열을 생성해 준다.
'''

ts= int(input())
for test_case in range(1,1+ts):
    ret=''
    A,B,C,D=list(map(int, input().split()))
    if B==0 and C==0 and A!=0 and D!=0:
        print('#{} impossible'.format(test_case))
        continue
    if B==0 and C==0 and A==0:
        ret='1'*(D+1)
        print('#{} {}'.format(test_case, ret))
        continue
    if B==0 and C==0 and D==0:
        ret='0'*(A+1)
        print('#{} {}'.format(test_case, ret))
        continue
    if abs(B-C) >1:
        print('#{} impossible'.format(test_case))
        continue
    if B==C:
        ret='1'*(D+1)
        for _ in range(B-1):
            ret+='01'
        ret+='0'*(A+1)
        ret+='1'
        print('#{} {}'.format(test_case, ret))
        continue
    if B-C==1:
        ret='0'*A
        for _ in range(B):
            ret+='01'
        ret+='1'*D
        print('#{} {}'.format(test_case, ret))
        continue
    if C-B==1:
        ret='1'*D
        for _ in range(C):
            ret+='10'
        ret+='0'*(A)
        print('#{} {}'.format(test_case, ret))
        continue