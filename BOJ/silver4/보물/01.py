import sys
sys.stdin = open("input.txt")

N = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
ret = 0
for i in range(N):
    ret += a[i]*b[i]

print(ret)
