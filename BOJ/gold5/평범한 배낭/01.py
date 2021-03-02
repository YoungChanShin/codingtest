import sys
sys.stdin = open('input.txt')

# 갯수, 무게
N,K = list(map(int,input().split()))
# 무게, 가치
things = [list(map(int,input().split())) for _ in range(N)]
max_val = 0

def bfs(w,v, depth):
    global max_val
    for i in range(depth, N):
        new_w = w+things[i][0]
        new_v = v+things[i][1]
        if new_w <= K:
            bfs(new_w,new_v, i+1)
            if new_v>max_val:
                max_val = new_v

bfs(0,0,0)
print(max_val)