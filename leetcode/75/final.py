# window에서 관리하는 데이터 : 새로 유입되는
import collections


def maxSlidingWindow(nums, k: int):
    if k == 1:
        return nums

    answer = []
    window = collections.deque()

    for idx, val in enumerate(nums):
        in_idx = idx
        out_idx = idx - k
        if window and window[0] == out_idx:
            window.popleft()
        while window and nums[window[-1]] < nums[in_idx]:
            window.pop()
        window.append(in_idx)

        if in_idx > k - 2:
            answer.append(nums[window[0]])

    return answer


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))


# 이제 이 풀이는 시간제한에 걸려서 통과되지 않는다.