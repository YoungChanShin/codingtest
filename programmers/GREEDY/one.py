def solution(number, k):
    answer = []
    i = 0
    for num in str(number):
        while k > 0 and len(answer) > 0 and answer[-1] < num:
            answer.pop(-1)
            k -= 1
        answer.append(num)

    if k > 0:
        answer = answer[: len(answer) - k]
    return "".join(answer)


nums = [1924, 1231234, 4177252841, 11]
ks = [2, 3, 4, 1]
for i in range(len(nums)):
    print(nums[i], ks[i])
    print(solution(nums[i], ks[i]))