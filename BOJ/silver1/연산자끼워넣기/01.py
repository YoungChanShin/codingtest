import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op = list(map(int,input().split()))

# (+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수
oper = ['+'] * op[0] + ['-'] * op[1]  + ['*'] * op[2] + ['//'] * op[3] 

def calc(nums, opers):
    ret = int(nums[0])
    for i in range(len(opers)):
        n = int(nums[i+1])
        if opers[i] == '+':
            ret += n
        elif opers[i] == '-':
            ret -= n
        elif opers[i] == '*':
            ret *= n
        elif opers[i] == '//':
            if ret<0:
                ret = (-ret)//n
                ret = -ret
            else:
                ret //= n
    return ret 

def oper_perm(arr,cnt,ret,checkList):
    if cnt == len(arr):
        opers.append(ret)
        return
    for i in range(len(arr)):
        if checkList[i]==0:
            checkList[i] = 1
            oper_perm(arr, cnt+1, ret+[str(arr[i])], checkList)
            checkList[i] = 0


opers = []

oper_perm(oper, 0, [], [0]*len(oper))


min_val = 1000000000
max_val = -1000000000
for o in opers:
    answer = calc(num,o)
    min_val = min(answer, min_val)
    max_val = max(answer, max_val)
print(max_val)
print(min_val)
