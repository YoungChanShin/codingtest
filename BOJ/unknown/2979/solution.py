import sys

sys.stdin = open('input.txt')

A,B,C = map(int,input().split())


answer = [0 for _ in range(101)]

for _ in range(3):
    arrive, depart = map(int,input().split())
    for i in range(arrive, depart):
        answer[i] += 1

sum = 0
for i in answer:
    if i == 3:
        sum += i*C
    elif i == 2:
        sum += i*B
    else:
        sum += i*A

print(sum)