import sys

N = int(sys.stdin.readline())
meetings = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
meetings = sorted(meetings)

max_val = 0 
# time 은 앞의 회의가 끝난 시간, depth는 몇번째 회의, meeting_idx는 진행 중인 회의의 index 인지 알려줌
def solution(time, depth, meeting_idx):
    global max_val
    if max_val<depth:
        max_val = depth

    for i in range(meeting_idx+1, N):
        if meetings[i][0]>=time:
            solution(meetings[i][1], depth+1,i)
solution(0,0,0)
print(max_val)