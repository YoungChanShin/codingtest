import sys
sys.stdin = open('input.txt')

def solution():
    N = int(input())
    data_list = [[] for _ in range(N)]
    populations = list(map(int,input().split()))
    for i in range(N): 
        area = list(map(int, input().split()))
        for j in range(1, area[0]+1):
            data_list[i].append(area[j]-1)
    # 대장 도시 정하기
    union = [-1 for _ in range(N)]

    # 두쪽으로 나누기


for _ in range(int(input())):
    solution()
