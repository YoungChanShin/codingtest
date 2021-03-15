import sys
sys.stdin = open('input.txt')

di = (0,0,-1,1)
dj = (1,-1,0,0)

def solution(cnt, wire, connected):
    global num_of_process, answer, connected_process
    N = len(maxinose)
    if cnt == num_of_process:
        if connected_process<connected:
            answer = wire
            connected_process = connected
        else:
            answer = min(wire, answer)
        return
    r,c = q[cnt]

    if r==0 or r==N-1 or c==0 or c==N-1:
        solution(cnt+1, wire, connected+1)
    
    else:
        for i in range(4):
            nr, nc = r+di[i],c+dj[i]
            new_wire = 0
            while -1<nr<N and -1<nc<N:
                if maxinose[nr][nc] != '0':
                    break
                maxinose[nr][nc] = '2'
                new_wire += 1
                nr += di[i]
                nc += dj[i]
            if nr==-1 or nr==N or nc==-1 or nc==N:
                solution(cnt+1, wire+new_wire, connected+1)
            # 전선 회수
            for j in range(new_wire):
                nr -= di[i]
                nc -= dj[i]
                maxinose[nr][nc] = '0'
    


for ts in range(int(input())):
    maxinose = [input().split() for _ in range(int(input()))]
    q = []
    answer = 1000
    connected_process = 0 
    N = len(maxinose)
    for i in range(N):
        for j in range(N):
            if maxinose[i][j]== '1':
                q.append((i,j))
    num_of_process = len(q)
    solution(0,0,0)
    print(f'#{ts+1} {answer}')