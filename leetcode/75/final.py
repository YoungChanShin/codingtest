# window에서 관리하는 데이터 : Dequeue until it encounters a value greater than the new data in the order of the most recently inserted data.
# 최근 삽입한 데이터 순서로 새 데이터보다 더 큰 값이 나올 때까지 큐에서 삭제
import collections


def maxSlidingWindow(nums, k: int):
    if k == 1:
        return nums

    answer = []  # return
    window = collections.deque()

    for idx, val in enumerate(nums):
        in_idx = idx
        out_idx = idx - k
        # 윈도우 밖의 데이터 삭제
        if window and window[0] == out_idx:
            window.popleft()

        # 최근에 삽입된 데이터의 순서로 새 데이터보다 큰 값을 만날 때까지 큐에서 빼기 - 결과적으로 내림차순
        while window and nums[window[-1]] < nums[in_idx]:
            window.pop()
        window.append(in_idx)

        if in_idx > k - 2:
            answer.append(nums[window[0]])

    return answer


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))