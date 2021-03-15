def can_pass(stones, k, h):
    zero_count = 0
    for i in range(len(stones)):
        y = max(0, stones[i] - h + 1)
        if y == 0:
            zero_count += 1
        else:
            zero_count = 0

        if zero_count >= k:
            return False

    return True

def solution(stones, k):
    low, high = 0, 200_000_001

    while low + 1 < high:
        mid = (low + high) // 2
        if can_pass(stones, k, mid):
            low = mid
        else:
            high = mid

    return low