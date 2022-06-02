from collections import defaultdict


def canFinish(numCourses: int, prerequisites) -> bool:
    req_graph = defaultdict(list)
    for req in prerequisites:
        a, b = req
        req_graph[a].append(b)
    for r in range(numCourses):
        if not dfs(req_graph, numCourses, r):
            return False
    return True


def dfs(req_graph, numCourses, root):
    visit = [0] * numCourses
    path = [(-1, root)]
    while path:
        req_node, this_node = path.pop()


numCourses = 2
prerequisites = [[1, 0]]
print(canFinish(numCourses, prerequisites))