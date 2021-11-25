# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# key = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
# key = [[0, 1], [1, 0]]
key = [[1] * 3 for _ in range(3)]
# lock = [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
lock = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
]


def rotate(square):
    # 시계 방향으로 회전하는 함수
    N = len(square)
    rotated = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[j][N - 1 - i] = square[i][j]
    return rotated


def match(key, lock, i, j):
    M = len(key)
    N = len(lock)
    for ii in range(N):
        for jj in range(N):
            if -1 < i + ii < M and -1 < j + jj < M:
                if lock[ii][jj] + key[i + ii][j + jj] != 1:
                    return False

            elif lock[ii][jj] != 1:
                return False
    return True


def solution(key, lock):
    # M <= N
    # key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
    # lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
    M = len(key)
    N = len(lock)
    keys = []
    for i in range(4):
        keys.append(key)
        key = rotate(key)

    r = range(-N + 1, M)

    for r_key in keys:
        for i in r:
            for j in r:
                if match(r_key, lock, i, j):
                    return True
    return False


print(solution(key, lock))