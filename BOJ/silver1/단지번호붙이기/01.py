import sys
sys.stdin = open("input.txt")

N = int(input())
apartments = [list(input()) for _ in range(N)]

d_row = [0,1,0,-1]
d_col = [1,0,-1,0]

cnt = 0
sizes = []

for i in range(N):
    for j in range(N):
        if apartments[i][j] == "1":
            size = 0
            cnt += 1
            s = [(i,j)]
            apartments[i][j] = "0"
            while s:
                row , col = s.pop()
                size += 1
                for k in range(4):
                    new_row = row+d_row[k]
                    new_col = col+d_col[k]
                    if -1<new_row<N and -1<new_col<N and apartments[new_row][new_col]=="1":
                        s.append((new_row,new_col))
                        apartments[new_row][new_col] = '0'
                        
            sizes.append(size)

sizes.sort()
print(cnt)
for i in sizes:
    print(i)
    