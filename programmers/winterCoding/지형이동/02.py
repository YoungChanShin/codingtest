from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
boundarise = []
def dfs(land, land_group, height, size_of_land, sr, sc, group_num):
    will_visit = deque()
    will_visit.append((sr,sc))
    while will_visit:
        row, col = will_visit.popleft()
        if land_group[row][col] == 0:
            land_group[row][col]= group_num
            for head in range(4):
                ni = row+di[head]
                nj = col+dj[head]
                if -1<ni<size_of_land and -1<nj<size_of_land:
                    if abs(land[row][col]-land[ni][nj])<=height:
                        will_visit.append((ni,nj))
                    else:
                        boundarise.append((abs(land[row][col]-land[ni][nj]), row, col, ni,nj))
                        
def getParent(u, v1):
    p = u[v1]
    while p != u[p]:
        p = u[p]
    return p

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

    boundarise.sort(key=lambda x: x[0])
    union = [i for i in range(group_num)]
    num_of_ladder = 0
    for b in boundarise:
        c = b[0]
        p1 = getParent(union, land_group[b[1]][b[2]])
        p2 = getParent(union, land_group[b[3]][b[4]])
        if getParent(union, p1) != getParent(union,p2):
            cost += c
            if p1<p2:
                union[p1] = p2
            else:
                union[p2] = p1
            num_of_ladder += 1
            if num_of_ladder == group_num-2:
                break
    return cost

# land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
# land = [[0,2,4],
#         [6,8,10],
#         [12,14,16]  
#     ]	
# land = [[1,2],[4,3]]
height = 1
print(solution(land, height))