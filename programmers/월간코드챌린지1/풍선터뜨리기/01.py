def solution(a):
    answer = 0
    n = len(a)
    ascending = [0]*n
    ascending[-1] = a[-1]
    for i in range(n-2,-1,-1):
        ascending[i] = min(ascending[i+1], a[i])

    descending = [0]*n
    descending[0] = a[0]
    for i in range(1,n):
        descending[i] = min(descending[i-1], a[i])

    result = set()
    for i in range(1,n-1):
        asc = ascending[i+1]
        decs = descending[i-1]
        if a[i] == max(a[i], asc,decs):
            result.add(asc)
            result.add(decs)
        else:
            result.add(asc)
            result.add(decs)
            result.add(a[i])

    return len(result)

a = [9,-1,-5]
a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
print(solution(a))