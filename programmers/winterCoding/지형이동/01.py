di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(land, land_group, height, size_of_land, sr, sc, group_num):
    visited = []
    will_visit = [(sr,sc)]
    while will_visit:
        row, col = will_visit.pop(0)
        if (row, col) not in visited:
            visited.append((row, col))
            land_group[row][col]= group_num
            for head in range(4):
                ni = row+di[head]
                nj = col+dj[head]
                if -1<ni<size_of_land and -1<nj<size_of_land:
                    if abs(land[row][col]-land[ni][nj])<=height:
                        will_visit.append((ni,nj))
                        

def solution(land, height):
    size_of_land = len(land)
    cost = 0
    land_group = [[0]*size_of_land for _ in range(size_of_land)]
    # 사다리 없이 이동가능한 영역끼리 그룹핑을 한다.(구역을 갯수를 안다.)
    group_num = 1
    for row in range(size_of_land):
        for col in range(size_of_land):
            if land_group[row][col] == 0:
                dfs(land, land_group, height, size_of_land, row, col, group_num)
                group_num+=1
    # union find 알고리즘
    parent = [0]
    for p in range(group_num):
        parent.append(p+1)
    def getParent(parent, child):
        if parent[child] == child:
            return child
        else:
            return getParent(parent, parent[child])
    def mergeUnion(parent, child1, child2):
        parent1 = getParent(parent, child1)
        parent2 = getParent(parent, child2)
        if parent1 == parent2:
            return
        elif parent1<parent2:
            parent[parent1] = parent2
        else:
            parent[parent2] = parent1

    def isUnion(parent, child1, child2):
        parent1 = getParent(parent, child1)
        parent2 = getParent(parent, child2)
        if parent1 == parent2:
            return True
        else:
            return False
    # 구역을 넘어갈 때 최소 비용을 기록한다.
    boundarise = []
    for row in range(size_of_land):
        for col in range(size_of_land):
            for head in range(4):
                ni = row+di[head]
                nj = col+dj[head]
                if -1<ni<size_of_land and  -1<nj<size_of_land:
                    if land_group[row][col] != land_group[ni][nj]:
                        flag = True
                        for b in boundarise:
                            if (b[0] == land_group[row][col] and b[1] == land_group[ni][nj]) or (b[0] == land_group[row][col] and b[1] == land_group[ni][nj]):
                                if b[2] > abs(land[row][col]-land[ni][nj]):
                                    boundarise.append((land_group[row][col], land_group[ni][nj], abs(land[row][col]-land[ni][nj])))
                                    flag = False
                        if boundarise == [] or flag:
                            boundarise.append((land_group[row][col], land_group[ni][nj], abs(land[row][col]-land[ni][nj])))
                        flag = True
    boundarise.sort(key=lambda x: x[2])
    # mst, 크루스칼 알고리즘을 이용해 사다리를 건설한다.
    for ladder in boundarise:
        if not isUnion(parent, ladder[0], ladder[1]):
            cost += ladder[2]
            mergeUnion(parent, ladder[0], ladder[1])
    
    return cost
land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]	
height = 3
print(solution(land, height))