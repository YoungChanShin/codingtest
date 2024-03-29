from collections import defaultdict


def findItinerary(tickets):
    graph = defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []

    def dfs(a):
        # 첫 번째 값을 읽어 어휘순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs("JFK")
    # 다시 뒤집어 어휘순 결과로
    return route[::-1]


tickets = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
print(findItinerary(tickets))