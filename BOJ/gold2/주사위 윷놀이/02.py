import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

maps = [[0]*4 for _ in range(43)]
horse = [[0,0] for _ in range(4)]

for i in range(0,41,2):
    maps[i][0] = i+2

# 10
for i in range(10,17,3):
    maps[i][1] = i+3
maps[19][1] = 25

# 20
maps[20][2] = 22
maps[22][2] = 24
maps[24][2] = 25

# 30 
maps[30][3] = 28
for i in range(28, 25, -1):
    maps[i][3] = i-1

# 25
for i in range(25, 40, 5):
    maps[i][1] = i+5

# 40
maps[40][0] = 42

# 도착
maps[42][0] = 100

# for i in range(len(maps)):
#     print(maps[i], i)

def move(_from_node, _to_step, line):
    cur = _from_node
    for i in range(_to_step):
        if cur > 40:
            break
        cur = maps[cur][line]
        if cur == 25:
            line = 1
        if cur == 40:
            line = 0
    if cur == 10:
        line = 1
    if cur == 20:
        line = 2
    if cur == 30 and line == 0:
        line = 3
    if cur == 25:
        line = 1
    return cur, line

dice = list(map(int, input().split()))

arr = [0]*10
answer = 0
def sum1(arr):
    s = 0
    for i in arr:
        if i < 42:
            s += i
        if i ==100:
            print("ERROR")
    return s

def solution(cnt):
    global answer
    if cnt == 10:
        return sum1(arr)
    for i in range(4):
        p, l = horse[i]
        if p > 40:
            continue
        np, nl = move(p, dice[cnt], l)            
        if [np, nl] in horse:
            if np != 42:
                continue
    
        arr[cnt] = np
        horse[i] = [np,nl]
        ret = solution(cnt+1)
        horse[i] = [p,l]
        answer = max(answer, ret)

    return sum1(arr[:cnt])

solution(0)
print(answer)