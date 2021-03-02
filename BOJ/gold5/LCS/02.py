import sys
sys.stdin = open('input.txt')

str1 = input()
str2 = input()
N = len(str1)
M = len(str2)

compare = [[0]*(N+1) for _ in range(M+1)]
for i in range(1,1+M):
    for j in range(1,1+N):
        if str2[i-1] == str1[j-1]:
            compare[i][j] = compare[i-1][j-1]+1
        else:
            compare[i][j] = max(compare[i-1][j], compare[i][j-1])

level = compare[M][N]        
print(level)

row = len(compare)-1
col = len(compare[0])-1
answer = ['']*level
while level>0:
    if compare[row][col-1]==level-1 and level-1 == compare[row-1][col]:
        answer[level-1] = str1[col-1]
        level -= 1
        row -= 1
        col -= 1
    elif compare[row][col] == compare[row-1][col]:
        row -= 1
    else:
        col -= 1
print("".join(answer))