def solution(land, P, Q):
    N = len(land)**2
    combined = []
    for i in land:
        combined.extend(i)
    combined.sort()
    cost = - combined[0]* N * Q + sum(combined) * Q
    answer = cost
    for i in range(1, N):
        if combined[i] != combined[i-1]:
            cost += (P * i - Q * (N-i)) * (combined[i] - combined[i-1])
            if cost > answer: break
            answer = cost
    return answer

# land = [[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]]
land = [[1,1,1], [1,1,1], [1,1,1]]
P = 5
Q = 3
print(solution(land, P, Q))