N =int(input())


def solution(N):
    cnt = 0 
    if N<100:
        print(N)
        return
    else:
        cnt = 99
        for i in range(111, N+1):
            hundred = i//100
            ten = (i//10)%10
            one = i % 10
            if ten-one == hundred-ten:
                cnt += 1
        print(cnt)

solution(N)