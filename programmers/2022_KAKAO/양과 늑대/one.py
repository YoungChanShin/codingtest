answer=0
def solution(info, edges):
    
    graph = [[ ] for i in range(len(info))]
    for p,ch in edges:
        graph[p].append(ch)
        
    def dfs(start = 0, candi=[], sheep=0, wolf=0):
        global answer
        sheep += 1 if info[start]==0 else 0
        wolf += info[start]
        answer = max(answer, sheep)
        
        if wolf >= sheep:
            return
        candi.extend(graph[start])
        for node in candi:
            newCandi = candi[:]
            newCandi.remove(node)
            dfs(node, newCandi,sheep, wolf)
    dfs()
    return answer