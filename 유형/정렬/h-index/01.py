def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    answer = n
    for i in range(n):
        if i + 1 == citations[i]:
            answer = i + 1
            break
        elif i + 1 > citations[i]:
            answer = i
            break

    return answer


citations = [3, 0, 6, 1, 5]
# citations = [1, 2, 3, 4, 5]
# citations = [5, 2, 3, 4, 1]
# citations = [5, 5, 5, 5, 5, 5, 5, 5]
# citations = [5, 5]
# citations = [1, 1, 1, 1]
# citations = [12, 11, 10, 9, 8, 1]

print(solution(citations))