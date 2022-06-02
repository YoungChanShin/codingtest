from collections import Counter


def getKeysNum(ct):
    ret = 0
    for k in ct:
        if ct[k] > 0:
            ret += 1
    return ret


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    left = 0
    ct = Counter()
    for right in range(len(cities)):
        newCity = cities[right].lower()
        if ct[newCity] > 0:  # HIT
            ct[newCity] += 1
            answer += 1

        else:  # miss
            ct[newCity] += 1
            answer += 5
            oldCity = cities[left].lower()
            while left + cacheSize <= right and (
                ct[oldCity] > 1 or getKeysNum(ct) > cacheSize
            ):
                ct[oldCity] -= 1
                left += 1
                oldCity = cities[left].lower()
    return answer


cacheSize = 0
# cities = [
#     "Jeju",
#     "Pangyo",
#     "Seoul",
#     "NewYork",
#     "LA",
#     "Jeju",
#     "Pangyo",
#     "Seoul",
#     "NewYork",
#     "LA",
# ]
cities = ["Jeju", "Jeju", "Jeju", "Jeju"]

print(solution(cacheSize, cities))
# arr = deque([1, 2, 3])
# print(list(arr)[1:])
# print(arr[0])
# arr.popleft()
# print(arr)