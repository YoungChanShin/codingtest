from collections import defaultdict, deque


def solution(times, n, k):
    map_dict = defaultdict(list)
    for edge in times:
        _from, _to, w = edge
        map_dict[_from].append((_to, w))
    print(map_dict)
    queue = deque()
    queue.append(map_dict[k])
    cnt = 1
    visited = [0] * (n + 1)
    print(queue)
    while cnt < n and queue:
        break


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

solution(times, n, k)