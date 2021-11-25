def solution(candidates, target):  # -> List[List[int]]
    answers = []

    def dfs(cur_idx, cur_val, elem):
        for idx in range(cur_idx, len(candidates)):
            if cur_val - candidates[idx] > 0:
                dfs(idx, cur_val - candidates[idx], elem + [candidates[idx]])
            elif cur_val - candidates[idx] == 0:
                answers.append(elem + [candidates[idx]])

    dfs(0, target, [])
    return answers


candidates = [2, 3, 6, 7]
target = 7
candidates = [2, 3, 5]
target = 8

print(solution(candidates, target))