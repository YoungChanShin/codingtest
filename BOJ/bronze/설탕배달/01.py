import sys

N = int(input())

init_5 = N//5

for i in range(init_5,-1,-1):
    if (N - i*5)%3 == 0:
        print(i+ (N - i*5)//3)
        sys.exit(0)
print(-1)