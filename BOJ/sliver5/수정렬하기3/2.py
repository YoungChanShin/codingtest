import sys
sys.stdin = open("input.txt")

N = int(sys.stdin.readline())
data_list = [0]*10001

for _ in range(N):
    data_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if data_list[i]!=0:
        for _ in range(data_list[i]):
            print(i)

'''
무조건 pypy가 빠른 것이 아니다
'''