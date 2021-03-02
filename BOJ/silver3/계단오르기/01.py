import sys
sys.stdin = open("input.txt")

N = int(input())
steps = [int(input()) for _ in range(N)]

# f[n]는 n-1계단을 밟지 않고 올라온 경우 얻는 경우
# f[n] = max(f[n-2], g[n-2]) + steps[n]

# g[n]는 n-1계단을 밟고 올라온 경우
# g[n] = f[n-1] + steps[n]

f = [0]*N
g = [0]*N

f[0] = steps[0]
g[0] = steps[0]

if N>1:
    f[1] = steps[1]
    g[1] = steps[0] + steps[1]


def get_f_num(num):
    if f[num] != 0:
        return f[num]
    f[num] = max(get_f_num(num-2), get_g_num(num-2)) + steps[num]
    return f[num]

def get_g_num(num):
    if g[num] != 0:
        return g[num]
    g[num] = get_f_num(num-1) + steps[num]
    return g[num]



def solution(num):
    return max(get_f_num(num-1), get_g_num(num-1))

print(solution(N))