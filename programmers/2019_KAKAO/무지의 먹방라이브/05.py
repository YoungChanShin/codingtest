def solution(food_times, k):
    n = len(food_times)
    s = 0
    sorted_food = []
    for i in range(n):
        sorted_food.append([i+1,food_times[i]])
        s += food_times[i]
    if k >= s:
        return -1
    sorted_food.sort(key=lambda x: x[1])
    i = 1
    acc = sorted_food[0][1] * n
    while k >= acc:
        k -= acc
        acc = (n - i) * (sorted_food[i][1] - sorted_food[i-1][1])
        i += 1    
    ret = sorted(sorted_food[i-1:], key=lambda x: x[0])
    return ret[k%len(ret)][0]

# food_times = [7,8,3,3,2,2,2,2,2,2,2,2] 
food_times = [1, 1, 2, 2, 5, 5, 5, 6] # n=8
k = 36
print(sum(food_times))
for i in range(sum(food_times)+1):
    print(solution(food_times, i), end = " ")