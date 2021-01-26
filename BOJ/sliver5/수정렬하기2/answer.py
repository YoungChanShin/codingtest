import sys
sys.stdin = open("input.txt")
N = int(input())
# data_list = [ sys.stdin.readline() for _ in range(N)]
data_list = [ int(input()) for _ in range(N)]
# data_list = sorted(list(map(lambda x: x.strip('\n'), data_list)))
data_list = sorted(data_list)
for i in data_list:
    print(i)