import sys

K,P,N = list(map(int,input().split()))

print(K*(P**N)%1000000007)