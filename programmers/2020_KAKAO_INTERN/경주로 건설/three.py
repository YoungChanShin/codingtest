from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def solution(board):
    answer = float('inf')
    N = len(board)
    visited = [
        [[float("inf"), float("inf"), float("inf"), float("inf")] for _ in range(N)]
        for _ in range(N)
    ]
    q = deque()

    def valid(r, c):
        return 0 <= r < N and 0 <= c < N

    visited[0][1][0] = 100
    q.append((100, 0, 1, 0))
    visited[1][0][1] = 100
    q.append((100, 1, 0, 1))

    while q:
        f, r, c, d = q.popleft()

        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if not valid(new_r, new_c):
                continue
            if board[new_r][new_c] == 1:
                continue
            cost = f + (100 if i == d else 600)
            if visited[new_r][new_c][i] >= cost:
                visited[new_r][new_c][i] = cost
                q.append((cost, new_r, new_c, i))
    answer = min(visited[N - 1][N - 1])
    return answer

board = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))