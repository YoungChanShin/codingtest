memo = [0]*1001
memo[1] = 1
memo[2] = 2

def solution(num):
    if memo[num]!=0:
        return memo[num]
    else:
        memo[num] = (solution(num-2)+solution(num-1))%10007
        return memo[num]

print(solution(int(input())))