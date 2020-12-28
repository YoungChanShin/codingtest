import sys
sys.stdin = open("input.txt", "r")

'''
1
4 5
1 2
2 3
3 2
4 4
부피 가치
'''
test_case = int(input())
def pick(items, idx, selected, remains):
    picked = 0
    if idx == len(items):
        return selected 

    volumn, value = items[idx][0], items[idx][1]
    if remains>= volumn:
        picked = pick(items, idx+1, selected+value, remains-volumn)

    unpicked = pick(items, idx+1, selected, remains)
    return max(picked, unpicked)


for ts in range(1, 1+test_case):
    N, K = map(int, input().split())
    items = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: x[0])
    print(f'#{ts} {pick(items, 0, 0, K)}')
