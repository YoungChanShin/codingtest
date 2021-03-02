import sys
sys.stdin = open("input.txt")

N = int(input())
data_list = []
for _ in range(N):
    # direction = input().split()
    direction = sys.stdin.readline().split()
    if direction[0] == 'push':
        data_list.append(direction[1])
    
    elif direction[0] == 'pop':
        print(data_list.pop() if len(data_list)>0 else -1)
    
    elif direction[0] == 'size':
        print(len(data_list))
    
    elif direction[0] == 'empty':
        print(0 if len(data_list)>0 else 1)
    
    elif direction[0] == 'top':
        print(data_list[-1] if len(data_list)>0 else -1)
    