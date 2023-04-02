import sys
sys.stdin = open('input.txt', 'r')

dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

def solution(dwarfs):
    for i in range(9):
        for j in range(i+1, 9):
            sum = 0
            for k in range(9):
                if i != k and j != k:
                    sum += dwarfs[k]
            if sum == 100:
                result = sorted(list(filter( lambda x: x not in (dwarfs[i],dwarfs[j]) ,dwarfs)))
                return result

for i in solution(dwarfs):
    print(i)