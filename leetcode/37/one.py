def solution(nums):
    ret = []

    def dfs(cur, elem):
        if cur >= len(nums):
            ret.append(elem)
        else:
            dfs(cur + 1, elem + [nums[cur]])
            dfs(cur + 1, elem)

    dfs(0, [])
    return ret


nums = [1, 2, 3]
print(solution(nums))
