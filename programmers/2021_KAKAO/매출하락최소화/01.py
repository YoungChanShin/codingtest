from collections import deque

# 그룹 내 참여자가 있는지 확인
def check(group, boss, check_list):
    for s in group[boss]:
        if check_list[s[0]-1]:
            return True
    return False

# 재귀적으로 완전탐색
def select(group, check_list, rev, min_revenue):
    if min_revenue < rev:
        return min_revenue
    flag = True
    for boss in group:
        # boss는 group key
        if not check(group, boss, check_list):
            flag = False
            for s in group[boss]:
                check_list[s[0]-1] = 1
                min_revenue = min(min_revenue, select(group, check_list, rev+s[1], min_revenue))
                check_list[s[0]-1] = 0
    if flag:
        min_revenue = min(min_revenue, rev)
    return min_revenue


    
def solution(sales,links):
    answer = 0
    group = dict()
    min_revenue = float('inf')
    for boss, staff in links:
        if boss in group.keys():
            group[boss].append([staff, sales[staff-1]])
        else:
            group[boss] = [[boss, sales[boss-1]], [staff, sales[staff-1]]]
    for g in group:
        group[g].sort(key=lambda x:x[1])
    check_list = [0]*len(sales)
    # select(group, check_list, rev)
    min_revenue = select(group, check_list, 0, min_revenue)
    
    return min_revenue

sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]	

sales = [5, 6, 5, 3, 4]
links = [[2,3], [1,4], [2,5], [1,2]]

sales = [5, 6, 5, 1, 4]
links = [[2,3], [1,4], [2,5], [1,2]]

sales = [10, 10, 1, 1]
links = [[3,2], [4,3], [1,4]]
print(solution(sales, links))