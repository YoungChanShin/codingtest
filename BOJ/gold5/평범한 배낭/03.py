# 메모이제이션
import sys
sys.stdin = open('input.txt')

N,K = list(map(int,input().split()))
board = [[-1]*(K+1) for _ in range(N+1)]
w = []
v = []
for _ in range(N):
    a,b = list(map(int,input().split()))
    w.append(a)
    v.append(b)

def solution(item, weight):
    if item==0 or weight==0:
        board[item][weight] = 0
        return 0
    if board[item][weight] != -1:
        return board[item][weight]
    
    if w[item-1] <= weight:
        board[item][weight] = max(solution(item-1, weight), v[item-1]+solution(item-1, weight-w[item-1]))
        return board[item][weight]
    
    board[item][weight] = solution(item-1, weight)
    return board[item][weight]

ret = solution(N,K)

print(ret)