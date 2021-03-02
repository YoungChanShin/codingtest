import sys
sys.stdin = open("input.txt")

N, M = list(map(int,input().split()))
# 4 2
data_list = sorted(list(map(int, input().split())))
# answer = [0]*M
visited = [0]*N

def solution(cnt, depth):
    global N,M
    if depth == M and cnt == N:
        print(visited)
        return
    if cnt > N or depth > M:
        return

    for i in range(0, N):

        if visited[i] == 0:
            solution(cnt+1, depth)
            visited[i] = 1
            solution(cnt+1, depth+1)
            visited[i] = 0

solution(0,0)