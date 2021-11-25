from collections import defaultdict


def findItinerary(tickets):
    path = ["JFK"]
    data_list = defaultdict(list)
    for _from, _to in sorted(tickets):
        data_list[_from].append(_to)

    _from = "JFK"
    for t in range(len(tickets)):
        _to = data_list[_from].pop(0)
        path.append(_to)
        _from = _to
    return path


# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
tickets = [
    ["JFK", "SFO"],
    ["JFK", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "JFK"],
    ["ATL", "SFO"],
]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

# tickets =[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# print(findItinerary(tickets))

tickets = [
    ["JFK", "BBB"],
    ["JFK", "DDD"],
    ["BBB", "CCC"],
    ["CCC", "JFK"],
    ["DDD", "JFK"],
]
print(findItinerary(tickets))