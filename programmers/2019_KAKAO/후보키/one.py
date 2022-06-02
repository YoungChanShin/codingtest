from itertools import combinations
from collections import defaultdict


def solution(relation):
    numOfData = len(relation)
    numOfCol = len(relation[0])
    possibleComb = []

    def checkIsMinimality(com):
        for p in possibleComb:
            if p.issubset(set(com)):
                return False
        return True

    def checkIsUniqueness(com, relation):
        data_dict = defaultdict(int)
        for s in relation:
            key = "".join([s[i] for i in range(numOfCol) if i in com])
            data_dict[key] += 1
            if data_dict[key] > 1:
                print(data_dict)
                return False
        print(data_dict)
        return True

    # 조합 뽑기
    for colSize in range(1, numOfCol + 1):
        combis = combinations(range(numOfCol), colSize)
        # 각 조합으로 후보키 가능한지 확인
        for com in combis:
            if not checkIsMinimality(com):
                continue

            if checkIsUniqueness(com, relation):
                possibleComb.append(set(com))
    return len(possibleComb)


relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"],
]
print(solution(relation))


print({1}.issubset({1, 2}))
