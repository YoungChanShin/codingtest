def solution(str1, str2):
    answer = 65536
    total = 0 # 합집합의 수와 교집합의 수를 더한 값을 저장한다.
    Ex = 0

    A_set = dict()
    Ex_set = dict()

    str1 = str1.lower()
    str2 = str2.lower()
    n = len(str1)
    for i in range(n-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            total += 1
            chuck = str1[i:i+2]
            if chuck in A_set.keys():
                A_set[chuck] += 1
            else:
                A_set[chuck] = 1

    n = len(str2)
    for i in range(n-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            total += 1
            chuck = str2[i:i+2]
            if chuck in A_set.keys():
                # Ex += 1
                if chuck in Ex_set.keys():
                    if Ex_set[chuck] < A_set[chuck]:
                        Ex += 1
                        Ex_set[chuck] += 1
                else:
                    Ex += 1
                    Ex_set[chuck] = 1

    if total == 0:
        return answer 
    return int(answer* (Ex / (total-Ex)))


str1 = "FRANCE"
str2 = "french"
print(solution(str1, str2))