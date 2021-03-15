def solution(food_times, k):
    n = len(food_times)
    s = 0
    sorted_food = []
    for i in range(n):
        sorted_food.append([i+1,food_times[i]])
        s += food_times[i]
    if k >= s:
        return -1
    sorted_food.sort(key=lambda x: (x[1]))
    height = 0
    i = 0
    while i < n:
        while k - (n-i) >= 0 and height < sorted_food[i][1]:
            height += 1
            k -= n-i

        if k - (n-i) < 0 and height < sorted_food[i][1]:
            ret = sorted_food[i:]
            ret.sort(key=lambda x: x[0])
            return ret[k][0]
        offset = 1
        while i+offset < n and sorted_food[i][1] == sorted_food[i+offset][1]:
            offset += 1
        i += offset
    return -1

food_times = [1, 1, 2, 2, 5, 5, 5, 6] # n=8
for i in range(sum(food_times)+5):
    print(solution(food_times, i))
# print(solution(food_times, 16))

# food_times = [3,1,2]
# print(solution(food_times, 5))