import sys
sys.stdin = open("input.txt")

N = int(input())

for _ in range(N):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    distance = (x2-x1)**2 + (y2-y1)**2
    diff = (r1-r2)**2
    plus = (r1+r2)**2
    if distance == 0 and diff==0:
        print(-1)
    elif distance > plus or distance < diff:
        print(0)
    
    elif distance == diff or plus == distance:
        print(1)

    else:
        print(2)