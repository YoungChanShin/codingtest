ts=int(input())
for test_case in range(1,1+ts):
    D,A,B,F=list(map(int, input().strip().split()))
    answer=D/(A+B) *F
    print('#{} {}'.format(test_case, answer))