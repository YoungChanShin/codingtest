import sys
sys.stdin = open("input.txt")

A = int(input())
students = list(map(int, input().split()))
d1, d2 = list(map(int,input().split()))

def cal(s):
    cnt = 0
    s = int(s)
    s -= d1
    cnt += 1
    if s > 0 :
        cnt += s//d2
        if s%d2>0:
            cnt += 1
    return cnt
students = list(map(cal, students))
print(sum(students))