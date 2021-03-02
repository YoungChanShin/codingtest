import sys

sys.stdin = open("input.txt")

from collections import deque

def solve(N,K):
    time = 0
    flag = True if N!=K else False

    q = deque()
    q.append(N)


    while flag:
        N = q.popleft()
        if N==K or N+1==K or N-1==K or N*2==K:
            flag = False
            return time
        else:
            if -1<N-1 and visited[N-1]==0:
                visited[N-1] = time+1
                q.append(N-1)
            if 2*N<100001 and visited[N*2]==0:
                visited[N*2] = time+1
                q.append(2*N)
            if N+1<100001 and visited[N+1]==0:
                q.append(N+1)
                visited[N+1] = time+1
        time+=1

if __name__=="__main__":
    N,K = list(map(int, input().split()))
    visited = [0]*100001
    visited[N] = 1
    print(solve(N,K))