import sys
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

meetings = sorted(meetings,key=lambda x: (x[1], x[0]))
print(meetings)
ret = 0
cnt = 0
for i in range(N):
    if ret <= meetings[i][0]:
        ret = meetings[i][1]
        cnt+=1
print(cnt)