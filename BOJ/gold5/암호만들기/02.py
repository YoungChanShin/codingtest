import sys
sys.stdin = open("input.txt")
from itertools import combinations

vowels = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, sys.stdin.readline().split())
pwd = sorted(list(map(str, sys.stdin.readline().split())))

comb = combinations(pwd, L)

def myprint(arr):
    for i in arr:
        print(i, end="")
    print()

for c in comb:
    count = 0
    for letter in c:
        if letter in vowels:
            count += 1

    if (count >= 1) and (count <= L-2):
        myprint(''.join(c))



'''
combinations를 쓰는 상황과 다르지 않다면 쓰는 것이 성능이 빠르다
여기서 검증하는 부분이 결국 마지막에 print직전에 있기 때문에 conbinations를 쓰는 것과 다르지 않다.
'''