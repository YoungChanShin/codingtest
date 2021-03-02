import sys
sys.stdin = open("input.txt")

from itertools import permutations, product

N, M = list(map(int,input().split()))

for i in list(product(list(range(1,N+1)) ,M)):
    arr = list(map(str,i))
    print(" ".join(arr))