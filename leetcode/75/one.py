def maxSlidingWindow(nums, k: int):
    if k == 1:
        return nums
    max_val = max(nums[:k])
    answer = [max_val]
    if max_val == nums[0]:
        max_val = max(nums[1:k])
    for i in range(1, len(nums) - (k - 1)):
        new_num = nums[i + k - 1]  # 윈도우로 새로 들어온 숫자
        old_num = nums[i]  # 앞으로 빠져나갈 숫자 - 아직 안 빠져 나감
        if new_num >= max_val:
            max_val = new_num
        answer.append(max_val)

        if old_num == max_val:
            max_val = max(nums[i + 1 : i + k])

    return answer


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))


# 이제 이 풀이는 시간제한에 걸려서 통과되지 않는다.