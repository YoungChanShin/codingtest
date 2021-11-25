# 메모리 초과
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M, T, K = map(int, input().split())  # N - 너비, M - 높이, T-금강석의 갯수, K-정사각형 크기
data_list = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
# 금강석 표시
for _ in range(T):
    A, B = map(int, input().split())
    data_list[B][A] = 1

# 너비 sliding window
b_window = [[0 for _ in range(N - K + 1)] for _ in range(M + 1)]
for row in range(M + 1):
    window = sum(data_list[row][: K + 1])
    b_window[row][0] = window
    for col in range(1, N - K + 1):
        window += data_list[row][col + K]
        window -= data_list[row][col - 1]
        b_window[row][col] = window

max_val = float("-inf")
max_val_row = -1
max_val_col = -1
# 깊이 sliding window
# d_window = [[0 for _ in range(N - K + 1)] for _ in range(M - K + 1)]
for col in range(N - K + 1):
    window = 0
    for ri in range(K + 1):
        window += b_window[ri][col]

    if max_val < window:
        max_val = window
        max_val_col = col
        max_val_row = row
    # d_window[0][col] = window
    for row in range(1, M - K + 1):
        window += b_window[row + K][col]
        window -= b_window[row - 1][col]
        if max_val < window:
            max_val = window
            max_val_col = col
            max_val_row = row
        # d_window[row][col] = window

print(max_val_col, max_val_row)
print(max_val)
