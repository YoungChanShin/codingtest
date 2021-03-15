def check(arr,k,n,l,r):
    # arr 배열에 있는 디딤돌이 없을 때 건널 수 있는지 확인, 할 수 있으면 False, 없으면 True
    # print(arr,len(arr), end = " ")
    if len(arr) < k:
        return False
    check_list = [0]*n 
    for i in arr:
        check_list[i[1]] = 1
    cnt = 0
    i = 0
    while i < n:
        if check_list[i] == 1:
            cnt += 1
            if cnt >= k:
                # print('True')
                return True
        else:
            cnt = 0
        i += 1
    # print('False')
    return False

def solution(stones, k):
    n = len(stones)
    sorted_stones = sorted([(s,i) for i,s in enumerate(stones)])
    if k == 1:
        return sorted_stones[0][0]
    elif k>n-1:
        return sorted_stones[-1][0]

    l = 0
    r = len(sorted_stones)-1
    while l<r :
        m = (l+r)//2
        if check(sorted_stones[:m],k,n,l,r):
            # 건널 수 없음
            r = m-1
        else:
            # 건널 수 있음
            l = m+1
    for i in (-1,0,1):
        if 0<l+i<n and check(sorted_stones[:l+i],k,n,l,r):
            return sorted_stones[l+i-1][0]
    
    return sorted_stones[l][0]
    # return sorted_stones[-1][0]

stones = [1, 1, 5, 2, 2, 3, 4, 1, 1, 1]
# stones = list(range(2,10000))
# stones = [1,1,3,5]
for i in range(1,len(stones)+1):
    print("answer",i,solution(stones,i))

# print(solution(stones,k))