def solution(food_times, k):
    answer = -1
    n = len(food_times)
    sorted_food = sorted([[i+1,f] for i,f in enumerate(food_times)], key=lambda x: (x[1]))
    height = 0
    tick = 0
    for i in range(n):
        if i == n-1:
            if sorted_food[i][1] == sorted_food[i-k][1] and i-k>=0:
                return sorted_food[i-tick+k][0]
            else:
                return -1
        if sorted_food[i][1] != sorted_food[i+1][1]:
            while k>0 and height < sorted_food[i][1]:
                k -= n-i
                height += 1
            if k > 0:
                tick = 0
                continue
            ret = sorted_food[i-tick:]
            ret.sort(key=lambda x: x[0])
            # print("k=",k, i,tick, ret,end="/ ")
            if k == 0:
                return ret[0][0]
            else:
                k += n-i
                # print(k)
                return ret[k][0]
        tick += 1
    return answer

# food_times = [3, 3, 3, 1, 2, 6, 1]
food_times = [1,1,1,2]
for i in range(sum(food_times)+2):
    # print(solution(food_times, i), end=" ")
    print(solution(food_times, i))