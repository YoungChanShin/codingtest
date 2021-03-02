import sys
sys.stdin = open("input.txt")

N =int(input())
links = [0]*(N+1)
check_list = [0]*(N+1)

for i in range(1,N+1):
    links[i] = int(input())

cnt = 0
for i in range(1, N+1):
    if check_list[i]==0:
        num_of_nodes = 0
        visited = []
        s = [i]
        start = 0
        while s:
            start = s.pop()
            if start not in visited:
                visited.append(start)
                s.append(links[start])
                num_of_nodes += 1
        if i == start:
            cnt += num_of_nodes
            for j in visited:
                check_list[j] = 1
print(cnt)
for i in range(1,1+N):
    if check_list[i]==1:
        print(i)