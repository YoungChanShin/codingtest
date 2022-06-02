import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

N, K = map(int, input().split())


def solution(N, K):
    dq = deque()
    dq.append((0, N))
    visited = [N]
    while dq:
        cnt, N = dq.popleft()
        if N - 1 > 0 and N - 1 not in visited:
            if N - 1 == K:
                return cnt + 1
            visited.append(N - 1)
            dq.append((cnt + 1, N - 1))

        if N + 1 not in visited:
            if N + 1 == K:
                return cnt + 1
            visited.append(N + 1)
            dq.append((cnt + 1, N + 1))

        if N < 100001 and N * 2 not in visited:
            if N * 2 == K:
                return cnt + 1
            visited.append(N * 2)
            dq.append((cnt, N * 2))


print(solution(N, K))
