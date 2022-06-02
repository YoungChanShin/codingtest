import sys
import heapq
from collections import defaultdict

sys.stdin = open("input.txt")
input = sys.stdin.readline

V, E = list(map(int, input().split()))


def solution(V, E):
    s = int(input())
    data_list = defaultdict(list)
    for _ in range(E):
        _from, _to, _weight = map(int, input().split())
        data_list[_from].append((_weight, _to))

    dist = [float("inf") for _ in range(V + 1)]
    pq = []
    heapq.heappush(pq, (0, s))
    dist[s] = 0
    # 다익스트라 알고리즘
    while pq:
        _weight, _to = heapq.heappop(pq)

        if dist[_to] < _weight:
            continue

        for w, next_node in data_list[_to]:
            next_wieght = w + _weight
            if dist[next_node] > next_wieght:
                dist[next_node] = next_wieght
                heapq.heappush(pq, (next_wieght, next_node))

    # 출력
    for vi in range(1, V + 1):
        if dist[vi] == float("inf"):
            print("INF")
        else:
            print(dist[vi])
    pass


solution(V, E)
