from itertools import combinations 
from collections import deque

import sys
sys.stdin = open('input.txt')

N,M,H = list(map(int,input().split()))

ladder = [list(map(int,input().split())) for _ in range(M)]
pick = deque()
pick.extend(ladder[:])
candidates = []

for i in range(1,N):
    for j in range(1,H+1):
        if [i,j] not in pick:
            candidates.append([j,i])

def go(si,sj):
    if [si,sj] in pick:
        return (si+1, sj+1)
    elif [si,sj-1] in pick:
        return (si+1, sj-1)
    else:
        return (si+1, sj)

def simulate():
    for i in range(1,N+1):
        si,sj = 0,i
        while si<=H:
            si,sj = go(si,sj)
        if sj == i:
            continue
        else:
            return False
    return True

def solution():
    # 0개 선택
    if simulate():
        return 0
    # 1개 선택
    for i in range(len(candidates)):
        pick.append(candidates[i])
        if simulate():
            return 1
        pick.pop()
    # 2개 선택
    for i in range(len(candidates)-1):
        pick.append(candidates[i])
        for j in range(i+1, len(candidates)):
            pick.append(candidates[j])
            if simulate():
                return 2
            pick.pop()
        pick.pop()
    # 3개 선택
    for i in range(len(candidates)-2):
        pick.append(candidates[i])
        for j in range(i+1, len(candidates)-1):
            pick.append(candidates[j])
            for k in range(j+1, len(candidates)):
                pick.append(candidates[k])
                if simulate():
                    return 3
                pick.pop()
            pick.pop()
        pick.pop()
    return -1

print(solution())