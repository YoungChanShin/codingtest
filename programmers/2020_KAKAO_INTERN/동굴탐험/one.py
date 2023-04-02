from collections import defaultdict

def solution(n, path, order):
    answer = True
    path = sorted([n if n[0]<n[1] else [n[1],n[0]] for n in path],key = lambda x: (x[0],x[1]))
    parent = defaultdict(int)
    for p,c in path:
        parent[c] = p
    
    prev = defaultdict(int)
    for p,c in order:
        prev[c] = p
    
    print(path)

    def getprev(s, f):
        result = True
        pa = parent[f]
        pr = prev[f]
        print(s,f,pa,pr)

        if pa == s or pr == s:
            return False
        if pa != 0:
            result = getprev(s, pa)
        if result and pr != 0:
            result = getprev(s, pr)
        return result

    for s in range(1,n):
        if getprev(s,s) == False:
            return False
        print("-----")

    return answer

n = 9
path = 	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]

path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[4,1],[8,7],[6,5]]
print(solution(n,path,order))