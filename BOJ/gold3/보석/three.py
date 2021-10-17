# 시간 초과 + 오답
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, M, T, K = map(int, input().split())  # N - 너비, M - 높이, T-금강석의 갯수, K-정사각형 크기
diamonds = []
# 금강석 표시
for _ in range(T):
    col, row = map(int, input().split())
    diamonds.append((row, col))

max_val = float("-inf")
max_val_row = -1
max_val_col = -1

for start_row in range(M - K + 1):
    window = []
    for col in range(K + 1):  # start_col = 0
        for row in range(start_row, start_row + K + 1):
            if (row, col) in diamonds:
                window.append((row, col))
        if max_val < len(window):
            max_val = len(window)
            max_val_col = 0
            max_val_row = start_row

    # 삭제 및 추가
    for start_col in range(1, M - K + 1):
        for row in range(start_row, start_row + K + 1):
            if (row, start_col + K) in diamonds:
                window.append((row, start_col))
            if (row, start_col - 1) in window:
                window.remove((row, start_col - 1))
        if max_val < len(window):
            max_val = len(window)
            max_val_col = start_col
            max_val_row = start_row

print(max_val_col, max_val_row)
print(max_val)