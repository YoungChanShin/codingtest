import sys
sys.stdin = open("input.txt")

import math

N = int(input())

def isPrime(num):
    if num < 2:
        return False
    start_num = int(math.sqrt(num))
    for i in range(2, start_num+1):
        if num % i == 0:
            return False
    return True

cnt = 0
data_list = list(map(int, input().split()))
for i in data_list:
    if isPrime(i):
        cnt += 1

print(cnt)
