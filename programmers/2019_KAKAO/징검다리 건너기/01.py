def check(arr,k,n):
    check_list = [0]*n
    for i in arr:
        idx = i[1]
        check_list[idx] = 1
        # cnt = 0
        # for j in range(-k+1,k):
        #     nj = j+idx
        #     if -1<nj<n and check_list[nj]==1:
        #         cnt += 1
        #         if cnt >= k:
        #             return True
        #     else:
        #         cnt = 0
    i = 0
    cnt = 0
    while i < n:
        if check_list[i] = 1:
            cnt += 1
            i += 1
            if cnt >= k:
                return True
        else:
            cnt = 0
    return False


def solution(stones, k):
    n = len(stones)
    sorted_stones = sorted([(s,i) for i,s in enumerate(stones)])
    # l = 0
    # r = len(sorted_stones)
    # while l<r:
    #     m = (l+r)//2
    #     if check(sorted_stones[:m],k,n):
    #         r = m-1
    #     else:
    #         l = m+1
    # return sorted_stones[l][0]-1
    i = 0
    height = sorted_stones[0][0]
    while i<n:


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

print(solution(stones,k))