import sys
sys.stdin = open("input.txt")
'''
4 2
9 8 7 1
'''
N, M = list(map(int, input().split()))
data_list = sorted(list(map(int, input().split())))
arr = [0]*M
def solution(cnt, depth):
    global N,M
    if depth == M:
        print(" ".join(map(str, arr)))
        return
    for i in range(cnt, N):
        arr[depth] = data_list[i]
        solution(i, depth+1)
solution(0,0)
# N,M = list(map(int,input().split()))
# data_list = sorted(list(map(int, input().split())))

# arr = [0]*M
# visited = [0]*N
# def solution(cnt, depth):
#     global N, M
#     if depth == M:
#         print(" ".join(map(str,arr)))
#         return
#     for i in range(cnt, N):
#         # if visited[i]==0:
#         arr[depth] = data_list[i]
#             # visited[i] = 1
#         solution(i, depth+1)
#             # visited[i] = 0

# solution(0,0)
# N ,M = list(map(int, input().split()))
# data_list = sorted(list(map(int,input().split())))
# arr =[0]*M

# def solution(depth):
#     global N,M
#     if M == depth:
#         print(" ".join(map(str, arr)))
#         return
#     for i in range(N):
#         arr[depth] = data_list[i]
#         solution(depth+1)
# solution(0)