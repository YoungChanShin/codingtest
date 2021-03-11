import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

paper = [input().split() for _ in range(10)]
p_5 = [0,5,5,5,5,5]

def isPossible(si, sj, size):
    if p_5[size]<1:
        return False
    for i in range(size):
        for j in range(size):
            ni = i+si
            nj = j+sj
            if -1<ni<10 and -1<nj<10 and paper[ni][nj] == '1':
                continue
            return False
    return True

sheets = 100
def solution(si,sh):
    # for i in paper:
    #     print(i)
    # print(sh)
    global sheets
    for i in range(10):
        for j in range(10):
            # 종료 조건
            if i==9 and j==9:
                # 마지막 칸이 1일때
                if paper[i][j] == '1':
                    # 1크기의 조각이 남아 있을 때
                    if p_5[1] > 0:
                        sh += 1
                    # 1크기의 조각이 남아 있지 않을 때
                    else:
                        return 100
                sheets = min(sh, sheets)
                return sheets

            if paper[i][j] == '1':
                flag = False
                for s in range(5,0,-1):
                    if isPossible(i,j,s):
                        flag = True
                        if sh+1>=sheets:
                            return 100
                        for x in range(i,i+s):
                            for y in range(j,j+s):
                                paper[x][y] = str(s*10)
                        p_5[s] -= 1
                        solution(si, sh+1)
                        for x in range(i,i+s):
                            for y in range(j,j+s):
                                paper[x][y] = '1'
                        p_5[s] += 1
                if flag == False:
                    return 100
                return
                        
solution(0,0)
print(sheets if sheets!=100 else -1)
# print(ret if ret != 100 else -1)
# print(sheets)