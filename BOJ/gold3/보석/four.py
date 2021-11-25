import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline
N, M, T, K = map(int, input().split())  # N - 너비, M - 높이, T-금강석의 갯수, K-정사각형 크기
diamonds = []
d_rows = []
d_cols = []
# 금강석 표시
for _ in range(T):
    col, row = map(int, input().split())
    diamonds.append((row, col))
    if row - K < 0:
        row = K
    if col + K > N:
        col = N - K
    d_rows.append(row)
    d_cols.append(col)

max_val = float("-inf")
max_val_col = -1
max_val_row = -1

for start_row in d_rows:
    for start_col in d_cols:
        diamond_cnt = 0
        for row, col in diamonds:
            if start_col <= col <= start_col + K and start_row - K <= row <= start_row:
                diamond_cnt += 1
        if diamond_cnt >= max_val:
            max_val = diamond_cnt
            max_val_col = start_col
            max_val_row = start_row

print(max_val_col, max_val_row)
print(max_val)