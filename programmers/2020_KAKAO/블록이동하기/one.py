import heapq

dr = [0,0,1,-1]
dc = [1,-1,0,0]
def solution(board):
    answer = 0
    r,c = 0,0
    visited = []
    hq = []
    heapq.heappush(hq,[0,r,c,0])
    heapq.heappush(hq,[0,r,c,2])
    print(hq)
    while hq:


    return answer


board =[[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))