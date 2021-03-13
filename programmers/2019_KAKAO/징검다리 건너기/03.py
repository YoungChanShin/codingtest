def check(check_list,k,n):
    cnt = 0
    i = 0
    while i < n:
        if check_list[i] == 1:
            cnt += 1
            if cnt >= k:
                return True
        else:
            cnt = 0
        i += 1
    return False


def solution(stones, k):
    n = len(stones)
    i = 0
    sorted_stones = sorted([(s,i) for i,s in enumerate(stones)])
    check_list = [0]*n

    while i<n-1:
        check_list[sorted_stones[i][1]] = 1
        if sorted_stones[i][0] == sorted_stones[i+1][0]:
            i += 1
            continue
        else:
            if check(check_list, k, n):
                return sorted_stones[i][0]
            i += 1
    check(check_list, k, n)
    return sorted_stones[-1][0]


stones = list(range(1000))
k = 100

print(solution(stones,k))